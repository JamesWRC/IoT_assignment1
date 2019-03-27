#!/usr/bin/python3
import MySQLdb
import time
from datetime import date
import sys
import numpy as np
import matplotlib.pyplot as plt

# open a database connection
connection = MySQLdb.connect(host="localhost", user="iot", passwd="Password123?", database="iot")

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# execute the SQL query using execute() method.
cursor.execute("SELECT temp, humidity, created_at FROM readings ORDER BY urid DESC LIMIT 5")

# fetch all of the rows from the query
rows = cursor.fetchall()

humidity = [] #create humidity array
temp = [] #create temp array
date = [] #create date array


rowCount = cursor.rowcount #total amount of rows
for row in rows:
    temp.append(row[0]) #loops through and adds temp to array
tupleTemp = tuple(temp) #casts from list to tuple

for row in rows:
    humidity.append(row[1]) #loops through and adds humidity to array
tupleHumidity = tuple(humidity)#casts from list to tuple

for row in rows:
    date.append(row[2].strftime("%m/%d\n%H-%M-%S")) #loops through and adds time, and format, to array
tupleDate = tuple(date)#casts from list to tuple


# create plot
fig, ax = plt.subplots()
index = np.arange(rowCount)
bar_width = 0.35 #sets the bar width
opacity = 0.8 #sets the bar visial opacity
 
tempBar = plt.bar(index, tupleTemp, bar_width, #params to construct the temprature bars
alpha=opacity,
color='g',
label='Temprature in °C')
 
humidityBar = plt.bar(index + bar_width, tupleHumidity, bar_width, #params to construct the humidity bars
alpha=opacity,
color='r',
label='Humidity in %')
 
plt.xlabel('Readings') #name for the x-axis label
plt.ylabel('Degrees °C / Humidity %') #name for the y-axis label
plt.title("Past {} Temprature / Humidity Readings".format(rowCount)) #name for the image graph title
plt.xticks(index + bar_width, tupleDate)
plt.legend()
plt.tight_layout()
plt.savefig('image.png') #saves the graph to an image, with image name passed in.
