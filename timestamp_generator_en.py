from datetime import datetime
from datetime import time
from datetime import date
import calendar
import time
import os
import sys
import subprocess
import math
import keyboard

print('''
   /$$      /$$  /$$$$$$   /$$$$$$  /$$                     /$$          
  | $$$    /$$$ /$$__  $$ /$$__  $$|__/                    |__/          
  | $$$$  /$$$$| $$  \__/| $$  \__/ /$$  /$$$$$$   /$$$$$$  /$$ /$$$$$$$ 
  | $$ $$/$$ $$| $$      | $$ /$$$$| $$ /$$__  $$ /$$__  $$| $$| $$__  $$
  | $$  $$$| $$| $$      | $$|_  $$| $$| $$  \__/| $$  \ $$| $$| $$  \ $$
  | $$\  $ | $$| $$    $$| $$  \ $$| $$| $$      | $$  | $$| $$| $$  | $$
  | $$ \/  | $$|  $$$$$$/|  $$$$$$/| $$| $$      |  $$$$$$$| $$| $$  | $$
  |__/     |__/ \______/  \______/ |__/|__/       \____  $$|__/|__/  |__/
                                                  /$$  \ $$              
                                                 |  $$$$$$/              
                                                  \______/               
''')

print("")
print(" This programme made by MCGirgin.")
print("")
print(" Place + for time zone.")
print(" Example usage:")
print(" +0300")

time.sleep(1)
print("")
print("")
print("")
def date_query():
	global day
	day = input(" DATE: ")
	if int(day) > 31 or int(day) < 1:
		print("")
		print(" Check your entry and try again.")
		print("")
		date_query()
	return day
date_query()

time.sleep(1)

def month_query():
	global ay, month, ay2, ay3
	ay = input(" MONTH: ")
	if ay == "january" or ay == "January" or ay == "Jan" or ay == "jan" or ay == "01" or ay == "1":
		month = "Jan"
		ay2 = "01"
		ay3 = "January"
		return month, ay2, ay3 

	elif ay == "february" or ay == "February" or ay == "Feb" or ay == "feb" or ay == "02" or ay == "2":
		month = "Feb"
		ay2 = "02"
		ay3 = "February"
		return month, ay2, ay3 

	elif ay == "march" or ay == "March" or ay == "Mar" or ay == "mar" or ay == "03" or ay == "3":
		month = "Mar"
		ay2 = "03"
		ay3 = "March"
		return month, ay2, ay3 

	elif ay == "april" or ay == "April" or ay == "Apr" or ay == "apr" or ay == "04" or ay == "4":
		month = "Apr"
		ay2 = "04"
		ay3 = "April"
		return month, ay2, ay3 

	elif ay == "may" or ay == "May" or ay == "05" or ay == "5":
		month = "May"
		ay2 = "05"
		ay3 = "May"
		return month, ay2, ay3 

	elif ay == "june" or ay == "June" or ay == "Jun" or ay == "jun" or ay == "06" or ay == "5":
		month = "Jun"
		ay2 = "06"
		ay3 = "June"
		return month, ay2, ay3 

	elif ay == "july" or ay == "July" or ay == "Jul" or ay == "jul" or ay == "07" or ay == "7":
		month = "Jul"
		ay2 = "07"
		ay3 = "July"
		return month, ay2, ay3 

	elif ay == "august" or ay == "August" or ay == "Aug" or ay == "aug" or ay == "08" or ay == "8":
		month = "Aug"
		ay2 = "08"
		ay3 = "August"
		return month, ay2, ay3 

	elif ay == "september" or ay == "September" or ay == "Sep" or ay == "sep" or ay == "09" or ay == "9":
		month = "Sep"
		ay2 = "09"
		ay3 = "September"
		return month, ay2, ay3 

	elif ay == "october" or ay == "October" or ay == "Oct" or ay == "oct" or ay == "10":
		month = "Oct"
		ay2 = "10"
		ay3 = "October"
		return month, ay2, ay3 

	elif ay == "november" or ay == "November" or ay == "Nov" or ay == "nov" or ay == "11":
		month = "Nov"
		ay2 = "11"
		ay3 = "November"
		return month, ay2, ay3 

	elif ay == "december" or ay == "December" or ay == "Dec" or ay == "dec" or ay == "12":
		month = "Dec"
		ay2 = "12"
		ay3 = "December"
		return month, ay2, ay3 
	else:
		print("")
		print(" Check your entry and try again.")
		print("")
		month_query()
month_query()

time.sleep(1)
year = input(" YEAR: ")
time.sleep(1)


def hour_query():
	global hour
	hour = input(" HOUR: ")
	if int(hour) > 23 or int(hour) < 0:
		print("")
		print(" Check your entry and try again.")
		print("")
		hour_query()
	elif int(hour) < 10 and len(hour) == 1:
		hour = "0{}".format(hour)
hour_query()


time.sleep(1)

def minute_query():
	global minute
	minute = input(" MINUTE: ")
	if int(minute) > 59 or int(minute) < 0:
		print("")
		print(" Check your entry and try again.")
		print("")
		minute_query()
	elif int(minute) < 10 and len(minute) == 1:
		minute = "0{}".format(minute)
minute_query()

def seconds_query():
	global seconds
	seconds = input(" SECONDS: ")
	if int(seconds) > 59 or int(seconds) < 0:
		print("")
		print(" Check your entry and try again.")
		print("")
		seconds_query()
	elif int(seconds) < 10 and len(seconds) == 1:
		seconds = "0{}".format(seconds)
seconds_query()

time.sleep(1)

def utc_query():
	global utc
	utc = input(" TIME ZONE: ")
	if utc.startswith("+") == False:
		print("")
		print(" Check your entry and try again.")
		print("")
		utc_query()
	elif len(utc) != 5:
		print("")
		print(" Check your entry and try again.")
		print("")
		utc_query()
	elif utc == "":
		utc = "+0000"
utc_query()

time.sleep(1)

date_String = "{}/{}/{} {}:{}:{} UTC {}".format(day, month, year, hour, minute, seconds, utc)
dt_format = datetime.strptime(date_String, "%d/%b/%Y %H:%M:%S %Z %z")
timestamp = dt_format.timestamp()
unix = "{}".format(timestamp)
unix = int(float(unix))

print("")
print(" --------------")
print(" | {} |".format(unix))
print(" --------------")
time.sleep(1)
print("")
print(" Discord")
print(" <t:{}>	 -  {} {} {} {}:{}".format(unix, day, ay3, year, hour, minute))
print(" <t:{}:t> - {}:{}".format(unix, hour, minute))
print(" <t:{}:T> - {}:{}:{}".format(unix, hour, minute, seconds))
print(" <t:{}:d> - {}/{}/{}".format(unix, day, ay2, year))
print(" <t:{}:D> - {} {} {}".format(unix, day, ay3, year))
print(" <t:{}:f> - {} {} {} {}:{}".format(unix, day, ay3, year, hour, minute))
weekday = dt_format.weekday()
if weekday == 0:
	weekday2 = "Monday"
if weekday == 1:
	weekday2 = "Tuesday"
if weekday == 2:
	weekday2 = "Wednesday"
if weekday == 3:
	weekday2 = "Thursday"
if weekday == 4:
	weekday2 = "Friday"
if weekday == 5:
	weekday2 = "Saturday"
if weekday == 6:
	weekday2 = "Sunday"
print(" <t:{}:F> - {}, {} {} {} {}:{}".format(unix, weekday2, day, ay, year, hour, minute))
print(" <t:{}:R> - Shows remaining time.".format(unix))
print("")
time.sleep(3)
x = input("Press enter to quit.")
print("")
if not x :
    print("Shutting down...")
    exit()