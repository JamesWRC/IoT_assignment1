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
    time = ""
    urid = ""
    status = ""
    min_humidity = ""
    
    #json file

   

    def __init__(self, temp, humidity, time, status): #reading constructor
        self.temp = temp
        self.humidity = humidity
        self.time = time
        self.status = status
        self.urid = hashlib.md5(self.time).hexdigest() #uses the current datetime and hashes it for a URID (Unique Reading Identifiation)


        with open('config.json') as f: #opens the config.json file
            config = json.load(f)
            self.min_humidity = config["min_humidity"] #gets the value of min_humidity from the file and assigns it to the instance variable



    def log(self): #simply logs/outputs the reading object into a nice human readable format.
        print("READING-LOG:\n =====================\n URID: {}\n =====================\n Temprature: {},\n Humidity: {},\n Timestamp: {},\n Status: {}\n".format(self.urid, self.temp, self.humidity, self.time, self.status))

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
reading = Reading(sense.get_temperature(), sense.get_humidity(), str(datetime.utcnow()), "NA") #creats a new reading object which passes in the temp, humidity, time and status as dictated form the SENSE_HAT
reading.checkStatus() #checks the humidity and updates the status based on min_humidity #Calls checkStatus



import MySQLdb #the bellow adds this object to a new row in the database.
import mysql.connector
db = MySQLdb.connect(host="localhost", user="iot", passwd="Password123?", db="iot")
mydb = mysql.connector.connect(host="localhost", user="root",passwd="Password123?",database="iot",port="3306")
mycursor = mydb.cursor()

sql = "INSERT INTO temps (temp, humidity, status) VALUES (%s, %s, %s)"
val = (reading.temp, reading.humidity, reading.status)
mycursor.execute(sql, val)

mydb.commit() #saves row in database based of object 

reading.log() #logs the object to the console