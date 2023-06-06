from selenium.webdriver.common.by import By
import time
import random
from . import SleepRandomLow


def doRandomStuff(driver):
    randomAction = random.randint(0, 4)
    if randomAction == 0:
        driver.find_element(By.LINK_TEXT, "Handlingslogg").click()
        time.sleep(SleepRandomLow.sleepRandomLow() * 2)
    elif randomAction == 1:
        driver.find_element(By.LINK_TEXT, "Salg/Søknad forum").click()
        time.sleep(SleepRandomLow.sleepRandomLow() * 2)
        elements = driver.find_elements(By.XPATH, "//a[contains(@href, 'index.php?p=viewthread&tid=')]")
        randomPick = random.randint(0, 9)
        if elements[randomPick].text == "↑" or elements[randomPick].text == "Salg og søknad":
            #do nothing
            print("Do nothing")
        else:
            time.sleep(SleepRandomLow.sleepRandomLow())
            elements[randomPick].click()
    elif randomAction == 2:
        driver.find_element(By.LINK_TEXT, "Dagens mord").click()
        time.sleep(SleepRandomLow.sleepRandomLow() * 2)
    elif randomAction == 3:
        driver.find_element(By.LINK_TEXT, "Innboks").click()
        time.sleep(SleepRandomLow.sleepRandomLow() * 2)
    else:
        driver.find_element(By.LINK_TEXT, "Generelt forum").click()
        time.sleep(SleepRandomLow.sleepRandomLow() * 2)
    time.sleep(5)
