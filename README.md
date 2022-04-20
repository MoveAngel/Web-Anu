# CRUD using FLask and SQLAlchemy 

## - Install requirement for project
```
pip install -r requirements.txt
```

## - Install virtualenv for project dependencies
```
virtualenv <name-env>
```

## - Create database and table
```
flask db init
```
### Then
```
flask db migrate
```
### And Last
```
flask db upgrade
```

## - Configure env file
```
FLASK_APP = run.py
FLASK_ENV = development
```

## Credits
* [piinalpin](https://github.com/piinalpin)