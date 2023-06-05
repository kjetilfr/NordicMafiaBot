from selenium.webdriver.common.by import By
import time
import random
from AntiBot import checkAntiBot
#from SleepRandomLow import sleepRandomLow
from CheckCountdown import checkCountdown


def sleepRandomLow():
    return random.randint(1, 3)

def utpress(driver):
    driver.find_element(By.LINK_TEXT, "Utpressing").click()
    checkAntiBot(driver)
    isCounting = checkCountdown(driver)
    if isCounting == False:
        # UTPRESSING START
        time.sleep(sleepRandomLow()/3)
        driver.find_element(By.ID, "sel_1").click()
        time.sleep(sleepRandomLow()/3)
        driver.find_element(By.NAME, "submitBlackmail").click()
        # UTPRESSING END
    else:
        print("Utpress timer is going")