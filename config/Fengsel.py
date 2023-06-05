from selenium.webdriver.common.by import By
import time
import random
from AntiBot import checkAntiBot
#from SleepRandomLow import sleepRandomLow
from CheckCountdown import checkCountdown
from DoRandomStuff import doRandomStuff


def sleepRandomLow():
    return random.randint(1, 3)

def fengsel(driver):
    driver.find_element(By.LINK_TEXT, "Fengsel").click()
    checkAntiBot(driver)
    isCounting = checkCountdown()
    if isCounting == False:
        time.sleep(sleepRandomLow() / 2)
        if len(driver.find_elements(By.LINK_TEXT, "Bryt ut")) > 0:
            driver.find_element(By.LINK_TEXT, "Bryt ut").click()
        else:
            time.sleep(random.randint(30, 69))
        time.sleep(3)
        doRandomStuff()
    else:
        print("Fengsel timer is going")