import psycopg2;

connection = psycopg2.connect("dbname=postgres")
cursor = connection.cursor()

cursor.execute(
    '''
    CREATE TABLE Employees(
        id INTEGER PRIMARY KEY,
        first_name VARCHAR NOT NULL,
        last_name VARCHAR NOT NULL,
        designation VARCHAR NOT NULL,
        full_time BOOLEAN NOT NULL
    );
    '''
)

cursor.execute(
    '''
    CREATE TABLE Paygrades(
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        employee_id INTEGER,
        FOREIGN KEY(employee_id) REFERENCES Employees(id)
    );
    '''
)

cursor.execute("INSERT INTO Employees (id, first_name, last_name, designation, full_time) VALUES (1, 'dayo', 'johnson', 'fe lead', true )")

cursor.execute("INSERT INTO Paygrades (id, name, employee_id) VALUES(1, 'senior analyst', 1)")

connection.commit()
cursor.close()
connection.close()



