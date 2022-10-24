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
print(" Bu program MCGirgin tarafından yapılmıştır.")
print("")
print(" Zaman diliminin başına + koyun.")
print(" Örnek kullanım:")
print(" +0300")

time.sleep(1)
print("")
print("")
print("")
def date_query():
	global day
	day = input(" Gün: ")
	if int(day) > 31 or int(day) < 1:
		print("")
		print(" Girdiğin değerleri kontrol et ve tekrar dene.")
		print("")
		date_query()
	return day
date_query()

time.sleep(1)

def month_query():
	global ay, month, ay2, ay3
	ay = input(" Ay: ")
	if ay == "ocak" or ay == "Ocak" or ay == "01" or ay == "1":
		month = "Jan"
		ay2 = "01"
		ay3 = "Ocak"
		return month, ay2, ay3 

	elif ay == "şubat" or ay == "Şubat" or ay == "Şub" or ay == "şub" or ay == "02" or ay == "2":
		month = "Feb"
		ay2 = "02"
		ay3 = "Şubat"
		return month, ay2, ay3 

	elif ay == "mart" or ay == "Mart" or ay == "Mar" or ay == "mar" or ay == "03" or ay == "3":
		month = "Mar"
		ay2 = "03"
		ay3 = "Mart"
		return month, ay2, ay3 

	elif ay == "nisan" or ay == "Nisan" or ay == "Nis" or ay == "nis" or ay == "04" or ay == "4":
		month = "Apr"
		ay2 = "04"
		ay3 = "Nisan"
		return month, ay2, ay3 

	elif ay == "mayıs" or ay == "Mayıs" or ay == "may" or ay == "May" or ay == "05" or ay == "5":
		month = "May"
		ay2 = "05"
		ay3 = "May"
		return month, ay2, ay3 

	elif ay == "haziran" or ay == "Haziran" or ay == "Haz" or ay == "haz" or ay == "06" or ay == "6":
		month = "Jun"
		ay2 = "06"
		ay3 = "Haziran"
		return month, ay2, ay3 

	elif ay == "temmuz" or ay == "Temmuz" or ay == "Tem" or ay == "tem" or ay == "07" or ay == "7":
		month = "Jul"
		ay2 = "07"
		ay3 = "Temmuz"
		return month, ay2, ay3 

	elif ay == "ağustos" or ay == "Ağustos" or ay == "Ağu" or ay == "ağu" or ay == "08" or ay == "8":
		month = "Aug"
		ay2 = "08"
		ay3 = "Ağustos"
		return month, ay2, ay3 

	elif ay == "eylül" or ay == "Eylül" or ay == "Eyl" or ay == "eyl" or ay == "09" or ay == "9":
		month = "Sep"
		ay2 = "09"
		ay3 = "Eylül"
		return month, ay2, ay3 

	elif ay == "ekim" or ay == "Ekim" or ay == "Ek" or ay == "ek" or ay == "10":
		month = "Oct"
		ay2 = "10"
		ay3 = "Ekim"
		return month, ay2, ay3 

	elif ay == "kasım" or ay == "Kasım" or ay == "Kas" or ay == "kas" or ay == "11":
		month = "Nov"
		ay2 = "11"
		ay3 = "Kasım"
		return month, ay2, ay3 

	elif ay == "aralık" or ay == "Aralık" or ay == "Ara" or ay == "ara" or ay == "12":
		month = "Dec"
		ay2 = "12"
		ay3 = "Aralık"
		return month, ay2, ay3 
	else:
		print("")
		print(" Girdiğin değerleri kontrol et ve tekrar dene.")
		print("")
		month_query()
month_query()

time.sleep(1)
def year_query():
	global year
	year = input(" YIL: ")
	if len(year) == 3:
		year = "0{}".format(year)
	elif len(year) == 2:
		year = "00{}".format(year)
	elif len(year) == 1:
		year = "000{}".format(year)
year_query()
time.sleep(1)


def hour_query():
	global hour
	hour = input(" SAAT: ")
	if int(hour) > 23 or int(hour) < 0:
		print("")
		print(" Girdiğin değerleri kontrol et ve tekrar dene.")
		print("")
		hour_query()
	elif int(hour) < 10 and len(hour) == 1:
		hour = "0{}".format(hour)
hour_query()


time.sleep(1)

def minute_query():
	global minute
	minute = input(" DAKİKA: ")
	if int(minute) > 59 or int(minute) < 0:
		print("")
		print(" Dakika 60'ın altında ve 0'ın üstünde (0 dahil) olmalı. Yani girdiğin değerleri kontrol et ve tekrar dene.")
		print("")
		minute_query()
	elif int(minute) < 10 and len(minute) == 1:
		minute = "0{}".format(minute)
minute_query()
time.sleep(1)
def seconds_query():
	global seconds
	seconds = input(" SANİYE: ")
	if int(seconds) > 59 or int(seconds) < 0:
		print("")
		print(" Dakika 60'ın altında ve 0'ın üstünde (0 dahil) olmalı. Yani girdiğin değerleri kontrol et ve tekrar dene.")
		print("")
		seconds_query()
	elif int(seconds) < 10 and len(seconds) == 1:
		seconds = "0{}".format(seconds)
seconds_query()

time.sleep(1)

def utc_query():
	global utc
	utc = input(" ZAMAN DİLİMİ: ")
	if utc.startswith("+") == False:
		print("")
		print(" Girdiğin değerleri kontrol et ve tekrar dene.")
		print("")
		utc_query()
	elif len(utc) != 5:
		print("")
		print(" Girdiğin değerleri kontrol et ve tekrar dene.")
		print("")
		utc_query()
	elif utc == "":
		utc = "+0000"
utc_query()

time.sleep(1)
try:
	date_String = "{}/{}/{} {}:{}:{} UTC {}".format(day, month, year, hour, minute, seconds, utc)
	dt_format = datetime.strptime(date_String, "%d/%b/%Y %H:%M:%S %Z %z")
	timestamp = dt_format.timestamp()
	unix = "{}".format(timestamp)
	unix = int(float(unix))
except Exception as e:
	print("")
	print(" Bir hata aldık ve program yeniden başlatılacak. Eğer girdiğin bütün\n değerler doğruysa lütfen Discord üzerinden MCGirgin#3953 ile iletişime geçin")
	time.sleep(5)
	print("")
	print(" Yeniden başlatılıyor...")
	time.sleep(3)
	print("")
	print("-------------------------------------")
	print("")
	subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:]) #restart the program

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
	weekday2 = "Pazartesi"
if weekday == 1:
	weekday2 = "Salı"
if weekday == 2:
	weekday2 = "Çarşamba"
if weekday == 3:
	weekday2 = "Perşembe"
if weekday == 4:
	weekday2 = "Cuma"
if weekday == 5:
	weekday2 = "Cumartesi"
if weekday == 6:
	weekday2 = "Pazar"
print(" <t:{}:F> - {}, {} {} {} {}:{}".format(unix, weekday2, day, ay, year, hour, minute))
print(" <t:{}:R> - Kalan zamanı gösterir.".format(unix))
print("")
time.sleep(3)
x = input("Çıkmak için Enter'a bas...")
print("")
if not x :
    print("Kapatılıyor...")
    exit()