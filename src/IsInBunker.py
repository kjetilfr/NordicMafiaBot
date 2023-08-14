from selenium.webdriver.common.by import By
import time
import random
import datetime
from . import GetTime
from . import IsLoggedIn

def sleepRandomLow():
    return random.randint(1, 3)


def inBunker(driver):
    if len(driver.find_elements(By.NAME, "dobuyout")) > 0:
        return True
    else:
        return False


def timeGetOutOfBunker(driver):
    try:
        timeanddate = driver.find_element(By.CSS_SELECTOR, "div.defpadding>span").get_attribute("innerHTML")
        clock = timeanddate[-8:]
        bunkerTime = clock.split(":")
        bunkerTimeTimeFormat = datetime.time(int(bunkerTime[0]), int(bunkerTime[1]), int(bunkerTime[2]))
        return bunkerTimeTimeFormat
    except:
        print("Cant get bunker time")


def bunker(driver):
    IsLoggedIn.checkLogin(driver)
    # TRY CATCH/EXCEPT IN CASE OF ERROR
    try:
        driver.find_element(By.LINK_TEXT, "Kriminalitet").click()
        if inBunker(driver):
            timeInBunker = timeGetOutOfBunker(driver)
            currentTime = GetTime.checkClock(driver)
            timeLeft = datetime.datetime.combine(datetime.datetime.today(), timeInBunker) - datetime.datetime.combine(
                datetime.datetime.today(), currentTime)
            print("Waiting " + str(timeLeft.total_seconds()) + " seconds")
            time.sleep(timeLeft.total_seconds())
            print("Sleeping additional 30 to 100 seconds random delay")
            time.sleep(random.randint(30, 100))
        else:
            print("Not in bunker")
    except:
        print("driver.find_element(By.LINK_TEXT, Kriminalitet).click() went wrong")