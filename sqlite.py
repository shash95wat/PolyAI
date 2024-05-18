import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("sqlite:///Chinook.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info=""" 
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)



## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from ''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()
