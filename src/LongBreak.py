import datetime
import time
from .GetTime import checkClock

from Settings import jsonRead


def getData():
    data = jsonRead.smallLoad()
    return data


def convertStringToTime(data):
    StringTime = data["settings"][3]["LongTimeoutTimerStart"]
    time_object = datetime.datetime.strptime(StringTime, '%H:%M:%S').time()
    return time_object

def addHoursToTime(time, hoursAdded):

    result = datetime.datetime.combine(datetime.datetime.today(), time) + datetime.timedelta(hours=hoursAdded)
    return result.time()

def isBetweenTime(driver):
    NordicMafiaTime = checkClock(driver)
    data = getData()
    LongTimeoutTimerStart = convertStringToTime(data)
    LongTimeoutTimerStop = addHoursToTime(LongTimeoutTimerStart, 0.5)
    print(str(LongTimeoutTimerStart) + " " + str(NordicMafiaTime) + " " + str(LongTimeoutTimerStop))
    if LongTimeoutTimerStart <= NordicMafiaTime <= LongTimeoutTimerStop:
        # SLEEP FOR A WHILE
        driver.get("https://facebook.com")
        # print("Sleeping for " + str(time.sleep(data["settings"][3]["LongTimeoutTimerInHours"] * 60 * 60)))
        time.sleep(4)
        driver.get("https://nordicmafia.org")
    else:
        # DONT SLEEP
        print("No longsleep")

