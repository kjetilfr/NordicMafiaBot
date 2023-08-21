from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import datetime
import random
from . import AntiBot
from . import SleepRandom
from . import CheckCountdown
from . import IsLoggedIn
from . import GetTime


def isBetweenTime(NordicMafiaTime):
    if datetime.time(21, 30, 00) <= NordicMafiaTime <= datetime.time(21, 50, 00):
        return True
    else:
        return False


def enterBunker(driver):
    try:
        driver.find_element(By.LINK_TEXT, "Eiendom").click()
    except:
        print('driver.find_element(By.LINK_TEXT, Eiendom).click() went wrong')
    IsLoggedIn.checkLogin(driver)
    AntiBot.checkAntiBot(driver)
    time.sleep(SleepRandom.sleepRandomLow() / 2)
    try:
        select = Select(driver.find_element(By.NAME, "numhours"))
    except:
        print("select = Select(driver.find_element(By.NAME, numhours) went wrong")
    time.sleep(SleepRandom.sleepRandomLow() / 4)
    try:
        select.select_by_value("2")
    except:
        print("select.select_by_value(2) went wrong")
    time.sleep(SleepRandom.sleepRandomLow() / 2)
    try:
        driver.find_element(By.NAME, "enterOwnBunker").click()
    except:
        print("driver.find_element(By.NAME, enterOwnBunker).click() went wrong")
    try:
        driver.switch_to.alert.accept()
    except:
        print("failed to accept bunker invite")
    print("sleep for " + str(7200 + random.randint(50, 200)))
    time.sleep(7200 + random.randint(50, 200))


def gaaIBunkerCheck(driver):
    IsLoggedIn.checkLogin(driver)
    if isBetweenTime(GetTime.checkClock(driver)):
        isCounting = CheckCountdown.checkCountdown(driver)
        if isCounting == False:
            enterBunker(driver)
        else:
            enterBunker(driver)
            time.sleep(300 + random.randint(10, 30))
    else:
        print("Some kind of timer is going")
