#!/usr/bin/python3
import MySQLdb
import time
from datetime import date
import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Analytics:
    rowCount = 0
    tupleTemp = ""
    tupleHumidity = ""
    tupleDate = ""

    def __init__(self):
        # open a database connection
        connection = MySQLdb.connect(host="localhost", user="iot", passwd="Password123?", database="iot")

        # prepare a cursor object using cursor() method
        cursor = connection.cursor()

        # execute the SQL query using execute() method.
        cursor.execute("SELECT temp, humidity, created_at FROM readings ORDER BY urid DESC LIMIT 5")

        # fetch all of the rows from the query
        rows = cursor.fetchall()

        # create humidity array
        humidity = []
        # create temp array
        temp = []
        # create date array
        date = []

        # total amount of rows
        self.rowCount = cursor.rowcount
        for row in rows:
            temp.append(row[0])  # loops through and adds temp to array
        self.tupleTemp = tuple(temp)  # casts from list to tuple

        for row in rows:
            humidity.append(row[1])  # loops through and adds humidity to array
        self.tupleHumidity = tuple(humidity)  # casts from list to tuple

        for row in rows:
            date.append(row[2].strftime("%m/%d\n%H-%M-%S"))  # loops through and adds time, and format, to array
        self.tupleDate = tuple(date)  # casts from list to tuple

    def graph_one(self):
        # create plot
        fig, ax = plt.subplots()
        index = np.arange(self.rowCount)

        # sets the bar width
        bar_width = 0.35

        # sets the bar visual opacity
        opacity = 0.8

        # params to construct the temperature bars
        tempBar = plt.bar(index, self.tupleTemp, bar_width,
                          alpha=opacity,
                          color='g',
                          label='Temperature in °C')

        # params to construct the humidity bars
        humidityBar = plt.bar(index + bar_width, self.tupleHumidity, bar_width,
                              alpha=opacity,
                              color='r',
                              label='Humidity in %')

        # name for the x-axis label
        plt.xlabel('Readings')

        # name for the y-axis label
        plt.ylabel('Degrees °C / Humidity %')

        # name for the image graph title
        plt.title("Past {} Temperature / Humidity Readings".format(self.rowCount))

        # Create names on the x-axis
        plt.xticks(index + bar_width, self.tupleDate)

        # Finalise the plot
        plt.legend()
        plt.tight_layout()

        # saves the graph to an image, with image name passed in.
        plt.savefig('plt.png')

    def graph_two(self):
        # Sets the background graph to white
        sns.set(style="white")

        # create suplot, there will be one figure and two graphs
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 5), sharex=True)

        # set every column show the date
        x = np.array(list(self.tupleDate))

        # Generate some sequential data
        tempBar = sns.barplot(x=x, y=self.tupleTemp, color='g', ax=ax1)
        humidityBar = sns.barplot(x=x, y=self.tupleHumidity, color='r', ax=ax2)

        ax1.axhline(0, color="k", clip_on=False)
        ax2.axhline(0, color="k", clip_on=False)

        # Labeling the graphs
        ax1.set_xlabel("Readings")
        ax1.set_ylabel("Degrees °C")

        ax2.set_xlabel("Readings")
        ax2.set_ylabel("Humidity %")

        # Finalise the plot
        plt.tight_layout()

        # saves the graph to an image, with image name passed in.
        plt.savefig('sns.png')


analytics = Analytics()
analytics.graph_one()
analytics.graph_two()
