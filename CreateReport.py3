#!/usr/bin/python3
import MySQLdb
import csv

# open a database connection
connection = MySQLdb.connect(host="localhost", user="iot", passwd="Password123?", database="iot")

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# execute the SQL query using execute() method. should be date and status
cursor.execute("select DATE_FORMAT(created_at, '%d/%m/%Y'), status, tempStatusMSG, humidityStatusMSG  from readings")

# fetch all of the rows from the query
data = cursor.fetchall()

# Creates a csv file
c = csv.writer(open("report.csv", "w"))

# write all the data in the report.csv
c.writerow(["Date", "Status"])
for row in data:
    c.writerow(row)