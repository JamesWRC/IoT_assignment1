#!/usr/bin/python3
################################
#  READ ME!
#  This file will dump the database to textfile so that I can use it for image graph in pyhton.
# Author: Sherry
#
################################

import os
import time


def grabData():

    user = "iot"
    password = "Password123?"
    host = "localhost"
    database = "iot"

    filestamp = time.strftime('%d-%m-%Y')
    os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | cat > data_%s.txt" % (user, password, host, database, filestamp))

if __name__ == "__main__":
    grabData()