import sqlite3

conn = sqlite3.connect("people.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS elployees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)  UNIQUE NOT NULL,
    email VARCHAR(40)  UNIQUE NOT NULL,
    date_of_birth TIMESTAMP DEFAULT NULL,
    age INT DEFAULT NULL,
    salary DECIMAL(10, 2) DEFAULT NULL
    );
''')

conn.commit()
conn.close()
