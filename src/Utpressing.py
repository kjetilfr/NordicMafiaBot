from selenium.webdriver.common.by import By
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn


def sleepRandomLow():
    return random.randint(1, 3)


def utforUtpress(driver):
    AntiBot.checkAntiBot(driver)
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        # UTPRESSING START
        time.sleep(sleepRandomLow() / 3)
        try:
            driver.find_element(By.ID, "sel_1").click()
        except:
            print("Biltyveri action 0 went wrong")
        time.sleep(sleepRandomLow() / 3)
        try:
            driver.find_element(By.NAME, "submitBlackmail").click()
        except:
            print("Biltyveri action 0 went wrong")
        # UTPRESSING END
    else:
        print("Utpress timer is going")


def utpress(driver):
    IsLoggedIn.checkLogin(driver)
    driver.find_element(By.LINK_TEXT, "Utpressing").click()
    if IsLoggedIn.checkLogin(driver):
        utforUtpress(driver)
    else:
        driver.find_element(By.LINK_TEXT, "Utpressing").click()
        utforUtpress(driver)
