from sense_hat import SenseHat
from datetime import datetime
import json
from pprint import pprint

sense = SenseHat()
#get temprature from sense hat
temp = sense.get_temperature()

#get humidity from sense hat
humidity = sense.get_humidity()

#get datetime in UTC
time = datetime.utcnow()


#json file


with open('config.json') as f:
    config = json.load(f)
    print(config["min_humidity"])

status = "BAD"

if float(config["min_humidity"] > humidity):
	status = "OK"



import MySQLdb
import mysql.connector
db = MySQLdb.connect(host="localhost", user="iot", passwd="Password123?", db="iot")
mydb = mysql.connector.connect(host="localhost", user="root",passwd="Password123?",database="iot",port="3306")
mycursor = mydb.cursor()

sql = "INSERT INTO temps (temp, humidity, status) VALUES (%s, %s, %s)"
val = (temp, humidity, status)
mycursor.execute(sql, val)

mydb.commit()

