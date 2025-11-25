CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(40) UNIQUE NOT NULL,
    date_of_birth DATE,
    age INT,
    salary DECIMAL(10, 2)
);


