from selenium.webdriver.common.by import By
import datetime
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def checkClock(driver):
    try:
        time.sleep(0.3)
        dateClock = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "mainClock")))
        clock = str(dateClock.get_attribute("innerHTML"))
        clock = clock[-8:]
        newTime = clock.split(":")
        nordicMafiaTimeTimeFormat = datetime.time(int(newTime[0]), int(newTime[1]), int(newTime[2]))
        return nordicMafiaTimeTimeFormat
    except:
        print("Could not get time!")
        return datetime.time(0, 0, 0)
