from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import datetime
import random
from . import AntiBot
from . import SleepRandomLow
from . import CheckCountdown


def isBetweenTime(NordicMafiaTime):
    if datetime.time(23, 30, 00) <= NordicMafiaTime <= datetime.time(23, 50, 00):
        return True
    else:
        return False


def checkClock(driver):
    dateClock = driver.find_element(By.ID, "mainClock")
    clock = str(dateClock.get_attribute("innerHTML"))
    clock = clock[-8:]
    newTime = clock.split(":")
    nordicMafiaTimeTimeFormat = datetime.time(int(newTime[0]), int(newTime[1]), int(newTime[2]))
    return nordicMafiaTimeTimeFormat


def enterBuncker(driver):
    driver.find_element(By.LINK_TEXT, "Eiendom").click()
    time.sleep(SleepRandomLow.sleepRandomLow() / 2)
    select = Select(driver.find_element(By.NAME, "numhours"))
    time.sleep(SleepRandomLow.sleepRandomLow() / 4)
    select.select_by_value("2")
    time.sleep(SleepRandomLow.sleepRandomLow() / 2)
    driver.find_element(By.NAME, "enterOwnBunker").click()
    driver.switch_to.alert.accept()
    print("sleep for " + str(7200 + random.randint(50, 200)))
    time.sleep(7200 + random.randint(50, 200))


def gaaIBunkerCheck(driver):
    AntiBot.checkAntiBot(driver)
    if isBetweenTime(checkClock(driver)):
        isCounting = CheckCountdown.checkCountdown(driver)
        if isCounting == False:
            enterBuncker(driver)
        else:
            enterBuncker(driver)
            time.sleep(300 + random.randint(10, 30))
    else:
        print("Some kind of timer is going")
