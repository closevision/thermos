# thermos

## Dependencies

### Packages
Using python virtual environment is advised. Afterwards use pip to install project depencies.
```
pip install -r requirements.txt
```

### Tools

#### SQLAlchemy basics
The following example shows database creation and basic object manipulation using SQLAlchemy from Python REPL.

Database Setup
```
from thermos import db
from models import User, Bookmark
db.create_all()
```

Creating database objects
```
>>> u=User(username="maros", email="maros.kukan@darkstar.click")
>>> db.session.add(u)
>>> db.session.commit()
>>> db.session.add(Bookmark(url="http://www.pluralsight.com", date=datetime.utcnow(), description="Hardcore Developer Training"))
>>> db.session.commit()
```

Retrieving database objects
```
>>> User.query.get(1)
>>> User.query.filter_by(username="maros").all()
```

#### SQLite
Optionally you can intall sqlite3 to open the created SQLite database file.
```
apt-get install sqlite3
```
```
sqlite3 thermos.db
sqlite> .tables
bookmark  user
sqlite> PRAGMA table_info(user);
0|id|INTEGER|1||1
1|username|VARCHAR(80)|0||0
2|email|VARCHAR(120)|0||0
sqlite> PRAGMA table_info(bookmark);
0|id|INTEGER|1||1
1|url|TEXT|1||0
2|date|DATETIME|0||0
3|description|VARCHAR(300)|0||0
sqlite> SELECT * from user;
1|maros|maros.kukan@darkstar.click
sqllite> .exit
```

### Environment variables
To successfully run a flask application, ensure you set the following environment variables.

#### Linux
```
export FLASK_APP=thermos.py
export FLASK_ENV=development
```

#### Windows
```
set FLASK_APP=thermos.py
set FLASK_ENV=development
```

## Running the application
Flask development server is useful during application development, but is not recommended for production deployment for scability reasons.
```
flask run
```


