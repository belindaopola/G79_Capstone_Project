import mysql.connector

# To create database on local machine
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='[yourpassword]',  # edit this with your MySQL password
)

my_cursor = mydb.cursor()
# uncomment to create new databases
# my_cursor.execute("CREATE DATABASE conversations")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
