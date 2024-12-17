'''
def gen():
    yield 1
    yield 2
    yield 3

for value in gen():
    print(value)


import sqlite3

conn = sqlite3.connect("test.db")

print("database created successful")

conn.execute("""CREATE TABLE IF NOT EXISTS COMPANY (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL);""")
print("table created successfully")

conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(1,'PAUL',32,'CALIFORNIA',20000.00)")
conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES(2,'ALLEN',22,'CALI',2000.00)")
conn.commit()
conn.close()

'''
import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect('test.db')
print("Opened database successfully")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")

df = pd.read_sql_query("SELECT id, name, address, salary from COMPANY", conn)

print(cursor, type(cursor))

for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print( "SALARY = ", row[3])

print("Operation done successfully")
print(df)
conn.close()

