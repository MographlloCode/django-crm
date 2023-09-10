# Install Mysql
# https://dev.mysql.com/downloads/installer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234',
)

# Prepare a cursor object

cursor_object = database.cursor()

# Create the database

cursor_object.execute('CREATE DATABASE boostco_db')

print("Database OK")