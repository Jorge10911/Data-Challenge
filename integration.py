import csv
import datetime
import psycopg2
import validators

conn = psycopg2.connect(
    dbname="employees_db",
    user="employer",
    password="password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

with open('data/employees.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
     first = row.get("FirstName", "").strip()
        last = row.get("LastName", "").strip()
    for row in reader:
        #get full name from first and last name
        if row[1] == '' or row[2] == '':
            continue
        name = f"{row[1]} {row[2]}"

        #ETL email
        if validators.email(row[3]):
            email = row[3]

        try:
            date_of_birth = datetime.datetime.strptime(row[5], '%d-%b-%y').date()
            age = datetime.datetime.now().year - date_of_birth.year
        except ValueError:
            date_of_birth = None
            age = None
        
        try: 
            salary = float(row[7].replace(',', ''))
            if salary < 0:
                salary = None
        except ValueError:
            salary = None

        cursor.execute("""
            INSERT INTO employees (name, email, date_of_birth, age, salary)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (email) DO NOTHING;
        """, (name, email, date_of_birth, age, salary))

conn.commit()
cursor.close()
conn.close()

print("ETL completed successfully")


