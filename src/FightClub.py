from selenium.webdriver.common.by import By
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn


def sleepRandomLow():
    return random.randint(1, 3)


def utforFightClub(driver):
    AntiBot.checkAntiBot(driver)
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        # FIGHTCLUB START
        time.sleep(sleepRandomLow() / 3)
        try:
            driver.find_element(By.XPATH, "//td[text()='25 pushups']").click()
        except:
            print("Fightclub action went wrong")
    else:
        print("Fightclub timer is going")


def fightclub(driver):
    IsLoggedIn.checkLogin(driver)
    driver.find_element(By.LINK_TEXT, "Fightclub").click()
    if IsLoggedIn.checkLogin(driver):
        utforFightClub(driver)
    else:
        driver.find_element(By.LINK_TEXT, "Fightclub").click()
        utforFightClub(driver)
