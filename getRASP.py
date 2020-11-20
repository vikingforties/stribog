# Stratus result...# http://rasp.mrsap.org/cgi-bin/get_rasp_blipspot.cgi?region=Thursday&grid=d2&day=0&lat=54.07356&lon=-1.90477&width=2000&height=2000&linfo=1&param=sfcsunpct%20sfctemp%20sfcdewpt%20mslpress%20sfcwinddir%20sfcwindspd%20blwindspd%20blwinddir%20rain1%20stars&format=JSON
# sfcsunpct%20sfctemp%20sfcdewpt%20mslpress%20sfcwinddir%20sfcwindspd%20blwindspd%20blwinddir%20rain1%20stars
# Locate it to the stations 1339 Shack - 54.05794 -2.22584 & 1159 YDSC 54.07356 -1.90477
# Data taken from http://rasp.stratus.org.uk/index.php/rasp-raw-data-by-day
# crontab this to run every morning after the model run  01 09 * * * python3 /home/pi/stribog/getRASP.py > /home/pi/stribog/faillog.txt 2>&1
# outputs to four files. The RASP0 file is for all of th todays and the RASP1 for allof the tomorows.
# To do:
# error handling
import requests
from datetime import date

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekdays += weekdays
holfuyStations = ["1339", "1159"]

for i in range(2):
    for station in holfuyStations:
        if station == "1339":
            r = requests.get('http://rasp.mrsap.org/cgi-bin/get_rasp_blipspot.cgi?region=' + weekdays[date.today().weekday() + i] +
                             '&grid=d2&day=0&lat=54.05794&lon=-2.2584&width=2000&height=2000&linfo=1&param=sfcsunpct%20sfctemp%20sfcdewpt%20mslpress%20sfcwinddir%20sfcwindspd%20blwindspd%20blwinddir%20rain1%20stars&format=JSON')
        else:
            r = requests.get('http://rasp.mrsap.org/cgi-bin/get_rasp_blipspot.cgi?region=' + weekdays[date.today().weekday() + i] +
                             '&grid=d2&day=0&lat=54.07356&lon=-1.90477&width=2000&height=2000&linfo=1&param=sfcsunpct%20sfctemp%20sfcdewpt%20mslpress%20sfcwinddir%20sfcwindspd%20blwindspd%20blwinddir%20rain1%20stars&format=JSON')
        with open("RASP" + str(i) + "_" + station + ".txt", "a") as logfile:
            logfile.write(str(r.json()))
            logfile.write("\n")
            logfile.close()
r.close()
