from random import randint
import MySQLdb
import mysql.connector
db = MySQLdb.connect(host="localhost", user="root", passwd="Password123?", db="iot")
mydb = mysql.connector.connect(host="localhost", user="root",passwd="Password123?",database="iot",port="3306")
mycursor = mydb.cursor()

sql = "UPDATE temps SET bmac = %s WHERE id = 1"
val = "RaNdOm Name: " + str(randint(0, 9999999))
mycursor.execute ("""
   UPDATE temps
   SET bmac=%s
   WHERE id=1
""", (val))

mydb.commit()

print(mycursor.rowcount, "record inserted.")
