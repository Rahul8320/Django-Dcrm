# for database creation

import mysql.connector

db = mysql.connector.connect(
	host = '127.0.0.1',
	user = 'root',
	passwd = 'password'
	)

# Prepare a cursor object
cursorObj = db.cursor()

# Create a database
cursorObj.execute("CREATE DATABASE dcrm")

print("DB Created Successfully!")