import sqlite3

conn = sqlite3.connect("user.db")
print("Database opened successfully")

conn.execute("create table Users(id INTEGER PRIMARY KEY AUTOINCREMENT, Username TEXT NOT NULL, EmailId VARCHAR UNIQUE NOT NULL, Password VARCHAR NOT NULL)")
print("Table created successfully")

conn.close()