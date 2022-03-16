# The Em_project

Takes logs of users having access to uploaded contents on a webpage. An email is sent to the admin and a log is recorded by the system in the database.

## How it works?

  1. User logs on to the system (Through the webpage).
  2. Users accesses the uploaded contents by a click.
  3. The system alerts the Admin of every access via an automated email.
  4. The database takes a log of every access and sorts them into their respective tables.

## Interactions with the System

1. Admin has the following priveleges:
* Log on to the system
* View the contents of the tables in the database
* View logins via mail
* Upload or delete contents

2. Users have the following priveleges:
* Log on to the system
* Access uploaded contents on the webpage

## Technologies used:

1. Front-end development:
* HTML
* CSS
* Javascript

2. Back-end development:
* Python
* Flask

3. Database:

* Sqlite3

## ====== Software & Tools Used ======
- VS Code
- Pycharm Community Edition
- SQLite3
- Python

*This is a sample project with a dummy database included in the project files*


## ===== Dummy Database Initialisation =====
1. Lauch Terminal in your IDE of choice
2. Navigate to the directory of the database
3. Copy and paste the following commands:
```
sqlite3
```
```
from app import db
```
```
db.tables
```

## Installation
1. With the above steps already executed
2. Open the python files in the IDE
3. Run app.py

**"Suggestions and improvements are invited"**
    Thanks a lot
    Ella_Emefa
    Project Leader
