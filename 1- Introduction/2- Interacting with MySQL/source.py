import mysql.connector

con = mysql.connector.connect(
user = "ReaderUser",
password = "reader",
host = "localhost",
database = "thesaurus_schema"
)

cursor = con.cursor()

word=input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM thesaurus_table WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")

# Get all users
# SELECT user FROM mysql.user;

# Remove an user
# DROP USER ReaderUser@localhost;
