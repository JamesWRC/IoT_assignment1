#!/usr/bin/python3

import MySQLdb
db = MySQLdb.connect(host="localhost",user="iot",passwd="Password123?",database="iot") #connection params
cursor = db.cursor() #connect to dbusing above params
cursor.execute("DROP TABLE IF EXISTS readings")
cursor.execute("CREATE TABLE readings (id BIGINT AUTO_INCREMENT PRIMARY KEY, urid VARCHAR(255), temp FLOAT, humidity FLOAT, status VARCHAR(255), tempStatusMSG VARCHAR(255), humidityStatusMSG VARCHAR(255), min_temp FLOAT, max_temp FLOAT, min_humidity FLOAT, max_humidity FLOAT, pushed BOOLEAN, created_at TIMESTAMP)")#creates table

cursor.execute("DROP TABLE IF EXISTS bluetooth")
cursor.execute("CREATE TABLE bluetooth (id BIGINT AUTO_INCREMENT PRIMARY KEY, ubid VARCHAR(255), devicemac VARCHAR(255), devicename VARCHAR(255), created_at TIMESTAMP, updated_at TIMESTAMP)")#creates table

#This file will create table name: readings

#TABLE readings IS CONSTRUCTED AS FOLLOWS
#<colname> : <datatype>
#id : BIGINT
#urid : string (VARCHAR)
#temp :float
#status : string (VARCHAR)
#tempStatusMSG : string (VARCHAR)
#humidityStatusMSG : string (VARCHAR)
#min_temp : float
#max_temp : float
#humidity : float
#min_humidity : float
#max_humidity : float
#pushed : boolean
#timestamps : Datetype

#TABLE bluetooth IS CONSTRUCTED AS FOLLOWS
#<colname> : <datatype>
#id : BIGINT
#ubid : string (VARCHAR) 
#pushed : boolean
#timestamps : Datetype

