from selenium.webdriver.common.by import By
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn

def sleepRandomLow():
    return random.randint(1, 3)

def krim(driver):
    driver.find_element(By.LINK_TEXT, "Kriminalitet").click()
    IsLoggedIn.checkLogin(driver)
    AntiBot.checkAntiBot(driver)
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        # KRIMINALITET START
        time.sleep(sleepRandomLow()/4)
        driver.find_element(By.ID, "rowid_table_select_krimaction4").click()
        # KRIMINALITET END
    else:
        print("Krim timer is going")