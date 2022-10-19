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

print("")
print(" Bu program MCGirgin tarafından yapılmıştır.")
print("")
print(" Ay parametresi dışında bütün parametreleri sayı şeklinde girebilirsiniz.")
print("")
print(" Ay parametresini tamamen küçük harflerle ve Türkçe bir şekilde yazınız.")
print("")
print(" Zaman dilimi için GMT, UTC yazmanıza gerek yok.  Sadece başına + koymanız lazım. Örneğin Türkiye +3 Zaman dilimini kullanır.")
print(" Bu zaman dilimi için dakikayı da girmek gerekir. Yani +03.00 olması lazım fakat bunu '.' olmadan yazmamız lazım.")
print(" Yani Türkiye Zaman dilimine göre girmek istiyorsanız +0300 yazmanız lazım. Farklı zaman dilimleri için de geçerlidir.")

time.sleep(1)
print("")
print("")
print("")
date = input(" GÜN: ")
time.sleep(1)

ay = input(" AY: ")

if ay == "ocak":
	month = "Jan"
	ay2 = "01"

elif ay == "şubat":
	month = "Feb"
	ay2 = "02"

elif ay == "mart":
	month = "Mar"
	ay2 = "03"

elif ay == "nisan":
	month = "Apr"
	ay2 = "04"

elif ay == "mayıs":
	month = "May"
	ay2 = "05"

elif ay == "haziran":
	month = "Jun"
	ay2 = "06"

elif ay == "temmuz":
	month = "Jul"
	ay2 = "07"

elif ay == "ağustos":
	month = "Aug"
	ay2 = "08"

elif ay == "eylül":
	month = "Sep"
	ay2 = "09"

elif ay == "ekim":
	month = "Oct"
	ay2 = "10"

elif ay == "kasım":
	month = "Nov"
	ay2 = "11"

elif ay == "aralık":
	month = "Dec"
	ay2 = "12"

time.sleep(1)
year = input(" YIL: ")
time.sleep(1)

hour = input(" SAAT: ")
time.sleep(1)

minute = input(" DAKİKA: ")
time.sleep(1)

seconds = input(" SANİYE: ")
time.sleep(1)

utc = input(" ZAMAN DİLİMİ: ")
time.sleep(1)

try:
	date_String = "{}/{}/{}:{}:{}:{} UTC {}".format(date, month, year, hour, minute, seconds, utc)
	dt_format = datetime.strptime(date_String, '%d/%b/%Y:%H:%M:%S %Z %z')
	timestamp = dt_format.timestamp()
	unix = "{}".format(timestamp)
	output = unix.split(".")
except Exception as e:
	print("")
	print("Bir hata aldık. Lütfen girdiğin değerleri kontrol et.")
	time.sleep(2)
	print("")
	print("Yeniden başlatılıyor...")
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
print(" <t:{}>	 -  {} {} {} {}:{}".format(output[0], date, ay, year, hour, minute))
print(" <t:{}:t> - {}:{}".format(output[0], hour, minute))
print(" <t:{}:T> - {}:{}:{}".format(output[0], hour, minute, seconds))
print(" <t:{}:d> - {}/{}/{}".format(output[0], date, ay2, year))
print(" <t:{}:D> - {} {} {}".format(output[0], date, ay, year))
print(" <t:{}:f> - {} {} {} {}:{}".format(output[0], date, ay, year, hour, minute))
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
print(" <t:{}:F> - {}, {} {} {} {}:{}".format(output[0], weekday2, date, ay, year, hour, minute))
print(" <t:{}:R> - Kalan zamanı sürkli değişen şekilde gösterir.".format(output[0]))
print("")
time.sleep(3)
x = input("Çıkmak için Enter tuşuna basınız.")
print("")
if not x :
    print("Kapatılıyor...")
    exit()