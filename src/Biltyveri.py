from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
from . import GetCity
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn
from . SleepRandom import sleepRandomLow


def sendCar(driver):
    currentCity = GetCity.getCity(driver)
    selectValue = random.randint(0, 5)
    time.sleep(sleepRandomLow())
    driver.find_element(By.XPATH, "//tr[@style='background-color: #ff4c4c;']").click()
    time.sleep(sleepRandomLow()/4)
    select = Select(driver.find_element(By.NAME, "targetcity"))
    time.sleep(sleepRandomLow()/4)
    select.select_by_value(str(selectValue))
    time.sleep(sleepRandomLow()/4)
    targetCity = select.first_selected_option.text
    print("'" + currentCity + "'" + " " + "'" + targetCity + "'")
    if targetCity == currentCity:  # if trying to send to current city restart function
        print("RETRYING TO SEND CAR!")
        driver.refresh()
        sendCar(driver)
    else:
        print("ACTUALLY SENDING CAR!")
        # actually send car
        time.sleep(sleepRandomLow())
        driver.find_element(By.NAME, "dotransport").click()
        time.sleep(sleepRandomLow())
        driver.find_element(By.NAME, "doTransport_confirm").click()


def biltyveri(driver):
    IsLoggedIn.checkLogin(driver)
    # BILTYVERI START
    driver.find_element(By.LINK_TEXT, "Biltyveri/Garasje").click()
    IsLoggedIn.checkLogin(driver)
    AntiBot.checkAntiBot(driver)
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        time.sleep(sleepRandomLow() / 2)
        driver.find_element(By.ID, "rowid_table_select_gtaaction0").click()
        biltyveriSuccess = driver.find_elements(By.CLASS_NAME, "successBox")
        if len(biltyveriSuccess) > 0:
            time.sleep(sleepRandomLow())
            sendCar(driver)
    else:
        time.sleep(sleepRandomLow())
        print("Car timer is going")