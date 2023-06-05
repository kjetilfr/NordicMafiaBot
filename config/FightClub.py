from selenium.webdriver.common.by import By
import time
import random
from AntiBot import checkAntiBot
from SleepRandomLow import sleepRandomLow
from CheckCountdown import checkCountdown


def sleepRandomLow():
    return random.randint(1, 3)

def sleepRandomLow():
    return random.randint(1, 3)


def fightclub(driver):
    driver.find_element(By.LINK_TEXT, "Fightclub").click()
    checkAntiBot(driver)
    isCounting = checkCountdown(driver)
    if isCounting == False:
        # FIGHTCLUB START
        time.sleep(sleepRandomLow()/3)
        driver.find_element(By.XPATH, "//td[text()='25 pushups']").click()
        # FIGHTCLUB END
    else:
        print("Fightclub timer is going")