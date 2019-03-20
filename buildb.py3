import MySQLdb
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="iot",passwd="Password123?",database="iot",port="3306") #connection params
mycursor = mydb.cursor() #connect to dbusing above params
mycursor.execute("CREATE TABLE temps (id BIGINT AUTO_INCREMENT PRIMARY KEY, temp FLOAT, humidity FLOAT, status VARCHAR(255), created_at TIMESTAMP, updated_at TIMESTAMP)")#creates table


#This file will create table name: temps

#TABLE TEMPS IS CONSTRUCTED AS FOLLOWS
#<colname> : <datatype>
#id : BIGINT
#temp :float
#humidity : float
#status : string (VARCHAR)
#timestamps : Datetype
