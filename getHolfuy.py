# crontab this to run every thirty minutes 01,31 * * * * python3 /home/pi/stribog/getholfuy.py > /home/pi/stribog/faillog.txt 2>&1
import requests
import json

holfuyStations = ["1339", "1159"]


def callStation(stationNumber):
    r = requests.get(
        'http://api.holfuy.com/live/?s=' + stationNumber + '&pw=gFuqC1CojBNOQq5&m=JSON&tu=C&su=m/s&utc&batt&su=mph')
    # print(r.content)
    # print(r.json()['wind']['speed'])
    json_r = json.loads(str(r.text))
    #print(json.dumps(json_r, indent=1))
    return(json_r)


def storeResults(results, stationNumber):
    with open("holfuy" + stationNumber + ".txt", "a") as logfile:
        logfile.write(str(results))
        logfile.write("\n")
        logfile.close()


for station in holfuyStations:
    storeResults(callStation(station), station)
r.close()
