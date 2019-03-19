import MySQLdb
import mysql.connector
db = MySQLdb.connect(host="localhost", user="root", passwd="Password123?", db="iot")
mydb = mysql.connector.connect(host="localhost", user="root",passwd="Password123?",database="iot",port="3306")
mycursor = mydb.cursor()

sql = "INSERT INTO temps (bmac, wmac) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
