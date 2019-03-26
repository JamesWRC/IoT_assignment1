#!/usr/bin/python3
import MySQLdb
import sys
from matplotlib import pyplot


connection = MySQLdb.connect(host="localhost", user="iot", passwd="Password123?", database="iot")

cursor = connection.cursor()

cursor.execute("select temp, humidity from temps")

data = cursor.fetchall()

for row in data:
    print(row[0], row[1])

label = ['Temperature', 'Humidity']

info = [row[0], row[1]]

pyplot.bar(label, info)

pyplot.xlabel('Name', fontsize=12)
pyplot.ylabel('Degree', fontsize=12)

pyplot.savefig('image.png')

cursor.close()

connection.close()

sys.exit()



