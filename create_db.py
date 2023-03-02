import mysql.connector

# # To create database on local machine
# mydb = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	passwd='password',  # edit this with your MySQL password
# 	)

# To create database on local machine
mydb = mysql.connector.connect(
	host="project-karty.cmoarzscfdhk.eu-west-2.rds.amazonaws.com",
	user="admin",
	passwd='3X47Qy!b',  # edit this with your AWS database instance password
	)


my_cursor = mydb.cursor()
# uncomment to create new databases
# my_cursor.execute("CREATE DATABASE users")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
	print(db)