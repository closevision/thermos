# thermos

## Dependencies

### Packages
Using python virtual environment is advised. Afterwards use pip to install project depencies.
```
pip install -r requirements.txt
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


