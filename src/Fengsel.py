from selenium.webdriver.common.by import By
import time
import random
from . import DoRandomStuff
from . import AntiBot
from . import CheckCountdown
from . import SleepRandomLow


def sleepRandomLow():
    return random.randint(1, 3)


def brytUt(driver):
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        time.sleep(sleepRandomLow() / 2)
        if len(driver.find_elements(By.LINK_TEXT, "Bryt ut")) > 0:
            driver.find_element(By.LINK_TEXT, "Bryt ut").click()
            time.sleep(SleepRandomLow.sleepRandomLow())
            brytUt(driver)
        else:
            time.sleep(random.randint(1, 2))
        DoRandomStuff.doRandomStuff(driver)
    else:
        print("Fengsel timer is going")


def fengsel(driver):
    driver.find_element(By.LINK_TEXT, "Fengsel").click()
    AntiBot.checkAntiBot(driver)
    brytUt(driver)
