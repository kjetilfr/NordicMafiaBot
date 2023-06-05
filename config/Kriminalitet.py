from selenium.webdriver.common.by import By
import time
import random
from AntiBot import checkAntiBot
#from SleepRandomLow import sleepRandomLow
from CheckCountdown import checkCountdown

def sleepRandomLow():
    return random.randint(1, 3)

def krim(driver):
    driver.find_element(By.LINK_TEXT, "Kriminalitet").click()
    checkAntiBot(driver)
    isCounting = checkCountdown(driver)
    if isCounting == False:
        # KRIMINALITET START
        time.sleep(sleepRandomLow()/4)
        driver.find_element(By.ID, "rowid_table_select_krimaction4").click()
        # KRIMINALITET END
    else:
        print("Krim timer is going")