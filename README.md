# ETL Script for Employees Database

This project loads employee data from a CSV file, applies basic validation and transformation, and stores the clean data in a SQLite database.

Requirements

Before running the program, make sure you have Python installed and the following packages:
```shell script
validators
```

If you do not have it installed, install it with:
```shell script
pip install -r requirements.txt
```
## What the Program Does

Creates a SQLite database named employees.db

Creates a table called employees

Reads data from data/employees.csv

Combines first and last name into one field

Validates email format

Converts date of birth into a date object and calculates age

Cleans salary values

Inserts valid records into the database

How to Run the Program

Place the employees.csv file inside the data folder.

Save the code in a Python file (example: main.py).

Run the script:
```shell script

python integration.py
```
or 
```shell script
python integration.py
```


After successful execution, the database file employees.db will be created with the cleaned employee data.

Output

If everything runs correctly, you will see:

ETL completed successfully
