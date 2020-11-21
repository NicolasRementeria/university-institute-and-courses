# Instead of working with the json data itself, as this json file can be too big and slow to handle and load, reducing the performance of the app.
# 
# In this case, we will change the approach by using a DataBase.

# Install "Mysql-connector-python" module with pip

# ex:
# pip install Mysql-connector-python

import mysql.connector

con = mysql.connector.connect(
user = "USERNAME",
password = "PASSWORD",
host = "DB_IP",
database = "DATABASE_NAME"
)

cursor = con.cursor()

word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)

results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("No word found!")