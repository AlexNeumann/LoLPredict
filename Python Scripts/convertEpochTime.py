# Code Written by: Alex Neumann
# CIS Honors Thesis
# Spring - Fall 2015 - Barrett Honors College

import datetime
from datetime import date
import time

#get the match creation time in epoch format
s = '1431337254631'
t = datetime.datetime.fromtimestamp(float(s)/1000.)

fmt = "%Y-%m-%d %H:%M:%S"

# convert from epoch to date format
dateOfMatch = t.strftime(fmt)[:10]
date1 = date(int(dateOfMatch[0:4]), int(dateOfMatch[5:7]), int(dateOfMatch[8:10]))

# get today's date
today = time.strftime("%Y-%m-%d")
date2 = date(int(today[0:4]), int(today[5:7]), int(today[8:10]))

print("Game was played on: " + str(date1))
print("Today's date: " + str(date2))

# calculate how many days ago the match was played
delta = date2 - date1
print("Game was played: " + str(delta.days) + " days ago...")
delta = delta.days

# if the match is older than 7 days skip this loop iteration
if delta <=7:
	print("The match is less than or equal to 7 days old")
else:
	print("This match is too old")
	


