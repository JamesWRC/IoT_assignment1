# IoT_assignment1



## Purpose
Purpose is to log weather and humidity into a database, send logged data to PushBullet, and to other devices via Bluetooth.
Represent this data into visual representation.
##### Join the Assignment PushBullet channel [here](https://www.pushbullet.com/channel?tag=IoT-s3656070)

## Important
We have used many libraries so please make sure you have the required libraries setup on your Raspberry Pi 3
- Install and setup MySQL
- Create a database called "iot" with the pasword of "Password123?"
- Run buildb.py3 - This will build the required tables for you. NOTE: Each time you run it, it will destroy the readings and bluetooth tables!!
- Run monitorAndNotify.py3 - This will create rows in the readings table of the current temp, humidity etc
- Once you have done these, you can run the rest of scripts as you wish.

## Assignment By
- s3656070 - James Cockshott
- s3656798 - Shahrzad Seyed Rafezi

## Languages used:
- Python3 - Used for the majority of the asignment.
- JSON - Used for communication between devices / services.
- MySQL - Used for database.

## Files included
- config.json
- monitorandnotify.py3
- createreport.py3
- bluetooth.py3
- analytics.py3
- analyticsreport.txt

## Check List
- [x] Task A
- [x] Task B
- [x] Task C
- [x] Task D
- [x] Task E


