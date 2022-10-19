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
date = input(" DATE: ")
if len(date) > 2:
	print("")
	print("Check your entry and try again.")
	time.sleep(2)
	print("")
	print("Restarting...")
	time.sleep(3)
	print("")
	print("-------------------------------------")
	print("")
	subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:]) #restart the program

time.sleep(1)

ay = input(" MONTH: ")

if ay == "january" or ay == "January" or ay == "Jan" or ay == "jan" or ay == "01" or ay == "1":
	month = "Jan"
	ay2 = "01"
	ay3 = "January"

elif ay == "february" or ay == "February" or ay == "Feb" or ay == "feb" or ay == "02" or ay == "2":
	month = "Feb"
	ay2 = "02"
	ay3 = "February"

elif ay == "march" or ay == "March" or ay == "Mar" or ay == "mar" or ay == "03" or ay == "3":
	month = "Mar"
	ay2 = "03"
	ay3 = "March"

elif ay == "april" or ay == "April" or ay == "Apr" or ay == "apr" or ay == "04" or ay == "4":
	month = "Apr"
	ay2 = "04"
	ay3 = "April"

elif ay == "may" or ay == "May" or ay == "05" or ay == "5":
	month = "May"
	ay2 = "05"
	ay3 = "May"

elif ay == "june" or ay == "June" or ay == "Jun" or ay == "jun" or ay == "06" or ay == "5":
	month = "Jun"
	ay2 = "06"
	ay3 = "June"

elif ay == "july" or ay == "July" or ay == "Jul" or ay == "jul" or ay == "07" or ay == "7":
	month = "Jul"
	ay2 = "07"
	ay3 = "July"

elif ay == "august" or ay == "August" or ay == "Aug" or ay == "aug" or ay == "08" or ay == "8":
	month = "Aug"
	ay2 = "08"
	ay3 = "August"

elif ay == "september" or ay == "September" or ay == "Sep" or ay == "sep" or ay == "09" or ay == "9":
	month = "Sep"
	ay2 = "09"
	ay3 = "September"

elif ay == "october" or ay == "October" or ay == "Oct" or ay == "oct" or ay == "10":
	month = "Oct"
	ay2 = "10"
	ay3 = "October"

elif ay == "november" or ay == "November" or ay == "Nov" or ay == "nov" or ay == "11":
	month = "Nov"
	ay2 = "11"
	ay3 = "November"

elif ay == "december" or ay == "December" or ay == "Dec" or ay == "dec" or ay == "12":
	month = "Dec"
	ay2 = "12"
	ay3 = "December"
else:
	print("")
	print("Check your entry and try again.")
	time.sleep(2)
	print("")
	print("Restarting...")
	time.sleep(3)
	print("")
	print("-------------------------------------")
	print("")
	subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:]) #restart the program

time.sleep(1)
year = input(" YEAR: ")
time.sleep(1)

hour = input(" HOUR: ")
if len(hour) > 2:
	print("")
	print("Check your entry and try again.")
	time.sleep(2)
	print("")
	print("Restarting...")
	time.sleep(3)
	print("")
	print("-------------------------------------")
	print("")
	subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:]) #restart the program

time.sleep(1)

minute = input(" MINUTE: ")
time.sleep(1)
if len(minute) > 2:
	print("")
	print("Check your entry and try again.")
	time.sleep(2)
	print("")
	print("Restarting...")
	time.sleep(3)
	print("")
	print("-------------------------------------")
	print("")
	subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:]) #restart the program

seconds = input(" SECONDS: ")
if len(seconds) > 2:
	print("")
	print("Check your entry and try again.")
	time.sleep(2)
	print("")
	print("Restarting...")
	time.sleep(3)
	print("")
	print("-------------------------------------")
	print("")
	subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:]) #restart the program
time.sleep(1)

utc = input(" TIME ZONE: ")
time.sleep(1)

try:
	date_String = "{}/{}/{}:{}:{}:{} UTC {}".format(date, month, year, hour, minute, seconds, utc)
	dt_format = datetime.strptime(date_String, '%d/%b/%Y:%H:%M:%S %Z %z')
	timestamp = dt_format.timestamp()
	unix = "{}".format(timestamp)
	output = unix.split(".")
except Exception as e:
	print("")
	print("Oops. We got an error. Check your entries and try again")
	time.sleep(2)
	print("")
	print("Restarting...")
	time.sleep(3)
	print("")
	print("-------------------------------------")
	print("")
	subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:]) #restart the program
	

print("")
print(" --------------")
print(" | {} |".format(output[0]))
print(" --------------")
time.sleep(1)
print("")
print(" Discord")
print(" <t:{}>	 -  {} {} {} {}:{}".format(output[0], date, ay3, year, hour, minute))
print(" <t:{}:t> - {}:{}".format(output[0], hour, minute))
print(" <t:{}:T> - {}:{}:{}".format(output[0], hour, minute, seconds))
print(" <t:{}:d> - {}/{}/{}".format(output[0], date, ay2, year))
print(" <t:{}:D> - {} {} {}".format(output[0], date, ay3, year))
print(" <t:{}:f> - {} {} {} {}:{}".format(output[0], date, ay3, year, hour, minute))
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
print(" <t:{}:F> - {}, {} {} {} {}:{}".format(output[0], weekday2, date, ay, year, hour, minute))
print(" <t:{}:R> - Shows remaining time.".format(output[0]))
print("")
time.sleep(3)
x = input("Press enter to quit.")
print("")
if not x :
    print("Shutting down...")
    exit()