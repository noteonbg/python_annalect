import sqlite3

connection = sqlite3.connect('my_database.db')  # 'my_database.db' is the database file

#prove that you have got connection

# Create a cursor object to execute SQL commands
cursor = connection.cursor()
print("ok")
cursor.close()
connection.close()
