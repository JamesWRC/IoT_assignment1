#!/usr/bin/python3
import MySQLdb
import sys
from matplotlib import pyplot

# open a database connection
connection = MySQLdb.connect(host="localhost", user="iot", passwd="Password123?", database="iot")

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# execute the SQL query using execute() method.
cursor.execute("select temp, humidity from temps")

# fetch all of the rows from the query
data = cursor.fetchall()

# print the rows in terminal for test purpose.
for row in data:
    print(row[0], row[1])

# Displays names for each column
label = ['Temperature', 'Humidity']

# Displays data in bar
info = [row[0], row[1]]

# Creates barChart
pyplot.bar(label, info)

# label for row
pyplot.xlabel('Name', fontsize=12)

# label for column
pyplot.ylabel('Degree', fontsize=12)

# creates an image from the graph
pyplot.savefig('image.png')

# close the cursor object
cursor.close()

# close the connection
connection.close()

# exit the program
sys.exit()



