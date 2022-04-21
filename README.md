# CRUD using Flask and SQLAlchemy 

## - Install virtualenv for project dependencies
```
virtualenv <name-env>
```

## - Install requirement for project
```
pip install -r requirements.txt
```

## - Configure env file
```
FLASK_APP = run.py
FLASK_ENV = development
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

## - Running the project
```
flask run
```

## Credits
* [piinalpin](https://github.com/piinalpin)