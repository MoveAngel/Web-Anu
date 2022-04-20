# CRUD using FLask and SQlAlchemy 

## - Install virtualenv for project dependencies
```
virtualenv <name-env>
```

## - Install requirement for project
```
pip install -r requirements.txt
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

## - Running the project
```
flask run
```

## Credits
* [piinalpin](https://github.com/piinalpin)