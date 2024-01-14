import sqlite3

#Connection
connection = sqlite3.connect("samp_employee.db")

#Creating cursor object
cursor = connection.cursor()

#Creating Table

table_dets = """
Create table EMPLOYEE(NAME VARCHAR(25), BIRTH_DATE DATE, LEVEL VARCHAR(10), HIRE_DATE DATE);
""" 

cursor.execute(table_dets)

cursor.execute('''INSERT INTO EMPLOYEE (NAME, BIRTH_DATE, LEVEL, HIRE_DATE) VALUES ('John Doe', '1990-05-15', 'ONE', '2022-01-01')''')
cursor.execute('''INSERT INTO EMPLOYEE (NAME, BIRTH_DATE, LEVEL, HIRE_DATE) VALUES ('Jane Smith', '1985-08-22', 'TWO', '2022-02-15')''')
cursor.execute('''INSERT INTO EMPLOYEE (NAME, BIRTH_DATE, LEVEL, HIRE_DATE) VALUES ('Bob Johnson', '1988-11-10', 'TWO', '2022-03-20')''')
cursor.execute('''INSERT INTO EMPLOYEE (NAME, BIRTH_DATE, LEVEL, HIRE_DATE) VALUES ('Alice Williams', '1995-03-05', 'THREE', '2022-04-10')''')


print("The inserted records are")

data = cursor.execute('''Select * From EMPLOYEE''')

for row in data:
    print(row)

connection.commit()
connection.close()

