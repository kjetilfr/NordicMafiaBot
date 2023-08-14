from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn
from . import DoRandomStuff


def sleepRandomLow():
    return random.randint(1, 3)


def utforLivvaktutleie(driver):
    AntiBot.checkAntiBot(driver)
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        time.sleep(sleepRandomLow() / 3)
        try:
            driver.find_element(By.NAME, "dowithdraw").click()
        except:
            print("Could not find dowithdraw element")
    else:
        print("Livvaktutleie timer is going")

def livvaktutleie(driver):
    IsLoggedIn.checkLogin(driver)
    # TRY CATCH/EXCEPT IN CASE OF ERROR
    try:
        driver.find_element(By.LINK_TEXT, "Livvaktutleie").click()
    except:
        print("driver.find_element(By.LINK_TEXT, Livvaktutleie).click() went wrong")
    if IsLoggedIn.checkLogin(driver):
        utforLivvaktutleie(driver)
    else:
        try:
            driver.find_element(By.LINK_TEXT, "Livvaktutleie").click()
        except:
            print("driver.find_element(By.LINK_TEXT, Livvaktutleie).click() went wrong 2")
        utforLivvaktutleie(driver)
