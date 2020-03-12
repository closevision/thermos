from datetime import datetime
import os

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from forms import BookmarkForm
import models

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')

# FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and 
# will be disabled by default in the future.  Set it to True or False to suppress this warning.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

bookmarks = []

def store_bookmark(url, description):
    bookmarks.append(dict(
        url = url,
        description = description,
        user = "maros",
        date = datetime.utcnow()
    ))

#def new_bookmarks(num):
#     '''Retrieves and sorts bookmarks from the list.'''
#    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]

@app.route('/')
@app.route('/index')
def index():
    #return render_template('index.html', new_bookmarks=new_bookmarks(5))
    return render_template('index.html', new_bookmarks=models.Bookmark.newest(5))

@app.route('/add', methods=['GET','POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        #Stored bookmarks in a list. 
        #store_bookmark(url, description)
        bm = models.Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        flash("Stored '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
