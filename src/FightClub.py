from selenium.webdriver.common.by import By
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn


def sleepRandomLow():
    return random.randint(1, 3)


def fightclub(driver):
    driver.find_element(By.LINK_TEXT, "Fightclub").click()
    IsLoggedIn.checkLogin(driver)
    AntiBot.checkAntiBot(driver)
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        # FIGHTCLUB START
        time.sleep(sleepRandomLow()/3)
        driver.find_element(By.XPATH, "//td[text()='25 pushups']").click()
        # FIGHTCLUB END
    else:
        print("Fightclub timer is going")