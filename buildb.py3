#!/usr/bin/python3

import MySQLdb
db = MySQLdb.connect(host="localhost",user="iot",passwd="Password123?",database="iot") #connection params
cursor = db.cursor() #connect to dbusing above params
cursor.execute("CREATE TABLE readings (id BIGINT AUTO_INCREMENT PRIMARY KEY, temp FLOAT, humidity FLOAT, status VARCHAR(255), min_temp FLOAT, max_temp FLOAT, min_humidity FLOAT, max_humidity FLOAT, created_at TIMESTAMP, updated_at TIMESTAMP)")#creates table


#This file will create table name: readings

#TABLE readings IS CONSTRUCTED AS FOLLOWS
#<colname> : <datatype>
#id : BIGINT
#temp :float
#min_temp : float
#max_temp : float
#humidity : float
#min_humidity : float
#max_humidity : float
#status : string (VARCHAR)
#timestamps : Datetype
