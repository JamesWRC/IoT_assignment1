#!/usr/bin/python3

from sense_hat import SenseHat
from datetime import datetime
import json
from pprint import pprint
import hashlib
sense = SenseHat()




#Create Class
class Reading:
    temp = 0.0
    humidity = 0.0
    urid = ""
    status = ""
    min_humidity = ""
    #json file

   

    def __init__(self, temp, humidity, status): #reading constructor
        self.temp = temp
        self.humidity = humidity
        self.status = status
        self.urid = hashlib.md5(str(datetime.utcnow()).encode('utf8')).hexdigest() #uses the current datetime and hashes it for a URID (Unique Reading Identifiation)

        with open('config.json') as f: #opens the config.json file
            config = json.load(f)
            self.min_humidity = config["min_humidity"] #gets the value of min_humidity from the file and assigns it to the instance variable

        self.min_temp = float(config["min_temperature"]) #sets object min_temp
        self.max_temp = float(config["max_temperature"]) #sets object max_temp
        self.min_humidity = float(config["min_humidity"]) #sets object min_humidity
        self.max_humidity = float(config["max_humidity"]) #sets object max_humidity

        '''
        The reason why we are setting the temperature and humidity paramaters (as shown above) is to easily compaire 
        the actual temps and humidity witht he params, rather then constantly opening and reading the 
        config.json file. 
        '''

    def log(self): #simply logs/outputs the reading object into a nice human readable format.
        print("READING-LOG:\n =====================\n URID: {}\n =====================\n Temprature: {},\n Humidity: {},\n Status: {},\n min_temp: {},\n max_temp: {},\n min_humidity: {},\n max_humidity: {},\n".format(
            self.urid, 
            self.temp, 
            self.humidity, 
            self.status, 
            self.min_temp, 
            self.max_temp, 
            self.min_humidity, 
            self.max_humidity))

    def setStatus(self, status): #sets the status on object
        self.status = status

    def checkStatus(self): #update status on object WILL REMOVE TOMORROW
        with open('config.json') as f: #opens the congig.json file
            config = json.load(f)
            self.config = config #assigns the object 

        if float(reading.min_humidity > reading.humidity):#if object humidity is less then the min humidity 
	        reading.setStatus("OK") #set the object status to OK

    
#Create object
#p1 = Reading(sense.get_temperature(), sense.get_humidity(), datetime.utcnow())
reading = Reading(sense.get_temperature(), sense.get_humidity(), "NA") #creats a new reading object which passes in the temp, humidity, time and status as dictated form the SENSE_HAT
reading.checkStatus() #checks the humidity and updates the status based on min_humidity #Calls checkStatus



import MySQLdb #the bellow adds this object to a new row in the database.
db = MySQLdb.connect(host="localhost", user="iot", passwd="Password123?", db="iot")
cursor = db.cursor()

sql = "INSERT INTO readings (temp, humidity, status, min_temp, max_temp, min_humidity, max_humidity) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (reading.temp, reading.humidity, reading.status, reading.min_temp, reading.max_temp, reading.min_humidity, reading.max_humidity)
cursor.execute(sql, val)

db.commit() #saves row in database based of object 

reading.log() #logs the object to the console


#NOTE IF YOURE HAVING ISSUES RUNNING THIS FILE PLEASE GO HERE DUE TO MySQLdb:
#https://raspberrypi.stackexchange.com/questions/78215/how-to-connect-mysqldb-in-python-3/78217