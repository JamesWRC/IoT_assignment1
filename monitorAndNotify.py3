#!/usr/bin/python3

from sense_hat import SenseHat
from datetime import datetime
import json
from pprint import pprint
import hashlib #for the md5 hash
import requests #for push bullet
import MySQLdb #for database

#Create Class
class Reading:
    
    temp = 0.0
    humidity = 0.0
    urid = ""
    status = ""
    tempStatusMSG = ""
    humidityStatusMSG = ""
    min_humidity = ""
    pushed = False

    """
    Overview:
        This Readings class simply constructs all the necessary attributes to be used for the other parts of the assignments:
            Bluetooth.py3
            CreateReport.py3
            analytics.py3
        Similarly these attributes are used to send notifications over the PushBullet API, to receive push notifications on all platforms such as, iOS, windows and so on.

    """


    def __init__(self, temp, humidity): #reading constructor
        self.temp = round(temp,1) #rounds temp to 1 decimal place.
        self.humidity = round(humidity,1) #rounds humidity to 1 decimal place.
        self.status = "OK"
        self.tempStatusMSG = "Temprature is within the specified parameters"
        self.humidityStatusMSG = "Humidity is within the specified parameters"

        self.urid = hashlib.md5(str(datetime.utcnow()).encode('utf8')).hexdigest() #uses the current datetime and hashes it for a URID (Unique Reading Identifiation)
       
        with open('config.json') as f: #opens the config.json file
            config = json.load(f)
            self.min_humidity = config["min_humidity"] #gets the value of min_humidity from the file and assigns it to the instance variable

        self.min_temp = float(config["min_temperature"]) #sets object min_temp
        self.max_temp = float(config["max_temperature"]) #sets object max_temp
        self.min_humidity = float(config["min_humidity"]) #sets object min_humidity
        self.max_humidity = float(config["max_humidity"]) #sets object max_humidity
        self.pushed = False

        """
        The reason why we are setting the temperature and humidity paramaters (as shown above) is to easily compare 
        the actual temps and humidity with the params, rather then constantly opening and reading the 
        config.json file. 
        """
        self.checkStatus() #checks and sets object status on creation


    def checkStatus(self): #sets the status on object
        if self.min_temp > self.temp:
            self.status = "BAD"
            self.tempStatusMSG = "The current temperature is {}{}C below the minimum temperature".format(round((self.min_temp - self.temp),1), '\xb0') #the params are as follows: temp difference, degree symbol
        if self.max_temp < self.temp:
            self.status = "BAD"
            self.tempStatusMSG = "The current temperature is {}{}C higher the maximum temperature".format(round((self.temp - self.max_temp),1), '\xb0') #the params are as follows: temp difference, degree symbol
        if self.min_humidity > self.humidity:
            self.status = "BAD"
            self.humidityStatusMSG = "The current humidity is {}% below the minimum humidity".format(round((((self.max_humidity - self.humidity)/self.max_humidity)*100),1)) #the params are as follows: temp difference, degree symbol
        if self.max_humidity < self.humidity:
            self.status = "BAD"
            self.humidityStatusMSG = "The current humidity is {}% higher the maximum humidity".format(round((((self.humidity - self.max_humidity)/self.humidity)*100),1)) #the params are as follows: temp difference, degree symbol
        
    def pushNotification(self):            
        headers = {'Access-Token': 'o.XE04vcyyRIYKWaqDhno27lsmcE0uxGXk', 'Content-Type': 'application/json'}
        payload = {'body':'Temperature: {},\n Humidity: {},\n Status: {},\n {},\n {}'.format(self.temp, self.humidity, self.status, self.tempStatusMSG, self.humidityStatusMSG),'title':'Weather Update','type':'note','channel_tag':'iot-s3656070'}
        response = requests.post("https://api.pushbullet.com/v2/pushes", json=payload, headers=headers)
        print("{}".format(response))
        if response.status_code == 200:
            print('Sent notification!')
            self.updatePushStatus(True) #set the object pushStatus to true to make sure it is only pushed once.
        else:
            raise Exception("ERROR: Could not send notification! Response Received: {}, check here for more information: https://docs.pushbullet.com/#http-status-codes".format(response))
    def addToDatabase(self):
        db = MySQLdb.connect(host="localhost", user="iot", passwd="Password123?", db="iot")
        cursor = db.cursor()

        sql = "INSERT INTO readings (urid, temp, humidity, status, tempStatusMSG, humidityStatusMSG, min_temp, max_temp, min_humidity, max_humidity, pushed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.urid, self.temp, self.humidity, self.status, self.tempStatusMSG, self.humidityStatusMSG, self.min_temp, self.max_temp, self.min_humidity, self.max_humidity, self.pushed)
        cursor.execute(sql, val)

        db.commit() #saves update the "pushed" atribute on the current row.
    def updatePushStatus(self, pushedStatus):
        self.pushed = pushedStatus
        db = MySQLdb.connect(host="localhost", user="iot", passwd="Password123?", db="iot")
        update = db.cursor()
        sql = "UPDATE readings SET pushed = %s WHERE urid = %s"
        val = (pushedStatus, self.urid)
        update.execute(sql, val)
        db.commit()

#Create object
reading = Reading(SenseHat().get_temperature(), SenseHat().get_humidity()) #creates a new reading object which passes in the temp, humidity, time and status as dictated form the SENSE_HAT
reading.addToDatabase() #adds object to database
reading.pushNotification() #sends a push notification about the reading.


#NOTE IF YOURE HAVING ISSUES RUNNING THIS FILE PLEASE GO HERE DUE TO MySQLdb:
#https://raspberrypi.stackexchange.com/questions/78215/how-to-connect-mysqldb-in-python-3/78217