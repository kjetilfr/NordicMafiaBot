from selenium.webdriver.common.by import By
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn


def sleepRandomLow():
    return random.randint(1, 3)


def utforKrim(driver):
    AntiBot.checkAntiBot(driver)
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        time.sleep(sleepRandomLow() / 3)
        try:
            oneinten = random.randint(1, 10)
            if oneinten != 10:
                driver.find_element(By.ID, "rowid_table_select_krimaction4").click()
            else:
                driver.find_element(By.ID, "rowid_table_select_krimaction0").click()
        except:
            print("Krim action 4 went wrong")
    else:
        print("Krim timer is going")

def krim(driver):
    IsLoggedIn.checkLogin(driver)
    driver.find_element(By.LINK_TEXT, "Kriminalitet").click()
    if IsLoggedIn.checkLogin(driver):
        utforKrim(driver)
    else:
        driver.find_element(By.LINK_TEXT, "Kriminalitet").click()
        utforKrim(driver)
