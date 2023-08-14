from selenium.webdriver.common.by import By
import datetime


def checkClock(driver):
    try:
        dateClock = driver.find_element(By.ID, "mainClock")
        clock = str(dateClock.get_attribute("innerHTML"))
        clock = clock[-8:]
        newTime = clock.split(":")
        nordicMafiaTimeTimeFormat = datetime.time(int(newTime[0]), int(newTime[1]), int(newTime[2]))
        return nordicMafiaTimeTimeFormat
    except:
        print("Could not get time!")
        return datetime.time(0, 0, 0)
