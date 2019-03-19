import MySQLdb
import mysql.connector
#James's pi db pass: "Password123?"
#Sherrys pi db pass: "raspberry"
mydb = mysql.connector.connect(host="10.132.114.117",user="iot",passwd="Password123?",database="iot",port="3306")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE temps (id BIGINT AUTO_INCREMENT PRIMARY KEY, bmac VARCHAR(255), wmac VARCHAR(255), temp FLOAT, humidity FLOAT, status VARCHAR(255), created_at TIMESTAMP, updated_at TIMESTAMP)")
print(mydb)


sql = "INSERT INTO temps (bmac, wmac, temp, humidity, status) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
