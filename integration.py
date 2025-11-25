import sqlite3
import csv
import datetime  
import re
import validators
regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"


conn = sqlite3.connect('employees.db')  # Make sure the filename ends with .db
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees;")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(40) UNIQUE NOT NULL,
    date_of_birth DATE,
    age INT,
    salary DECIMAL(10, 2)
)
''')


with open('data/employees.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:

        #get full name from first and last name
    
        name = f"{row['FIRST_NAME']} {row['LAST_NAME']}"

        #ETL email
        if validators.email(row['EMAIL']):
            email = row['EMAIL']
        else: 
            continue

        try:
            date_of_birth = datetime.datetime.strptime(row['DATE_OF_BIRTH'], '%d-%b-%y').date()
            age = datetime.datetime.now().year - date_of_birth.year
        except ValueError:
            date_of_birth = None
            age = None
        
        try: 
            salary = float(row['SALARY'].replace(',', ''))
            if salary < 0:
                salary = None
        except ValueError:
            salary = None

        cursor.execute("""
            INSERT OR IGNORE INTO employees (name, email, date_of_birth, age, salary)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, date_of_birth, age, salary))

conn.commit()
cursor.close()
conn.close()

print("ETL completed successfully")


