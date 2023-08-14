from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
from . import GetCity
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn
from . SleepRandom import sleepRandomLow
from . import DoRandomStuff


def sendCar(driver):
    time.sleep(sleepRandomLow() / 3)
    currentCity = GetCity.getCity(driver)
    selectValue = random.randint(0, 5)
    time.sleep(sleepRandomLow() / 3)
    # TRY CATCH/EXCEPT IN CASE OF ERROR
    try:
        elems = driver.find_elements(By.CSS_SELECTOR, "table.def_table.cursor>tbody>tr")
        carElems = []
        for i in elems:
            if not i.get_attribute("name") == "hlrow_table_select_gtaaction":
                carElems.append(i)

        for c in carElems:
            if c.get_attribute("style") == "background-color: #ff4c4c;" or c.get_attribute(
                    "style") == "background-color: rgb(255, 76, 76);":
                clickElem = c.find_element(By.CSS_SELECTOR, "td")
                clickElem.click()
            else:
                pass
    except:
        print("driver.find_element(By.XPATH, //tr[@style='background-color: #ff4c4c;']).click() went wrong")
    time.sleep(sleepRandomLow()/4)
    # TRY CATCH/EXCEPT IN CASE OF ERROR
    try:
        select = Select(driver.find_element(By.NAME, "targetcity"))
    except:
        print("select = Select(driver.find_element(By.NAME, targetcity)) went wrong")
    time.sleep(sleepRandomLow() / 4)
    select.select_by_value(str(selectValue))
    time.sleep(sleepRandomLow() / 4)
    targetCity = select.first_selected_option.text
    print("'" + currentCity + "'" + " " + "'" + targetCity + "'")
    # if trying to send to current city restart send function
    if targetCity == currentCity:
        print("RETRYING TO SEND CAR!")
        driver.refresh()
        sendCar(driver)
    else:
        print("ACTUALLY SENDING CAR!")
        # actually send car
        time.sleep(sleepRandomLow() / 3)
        # TRY CATCH/EXCEPT IN CASE OF ERROR
        try:
            driver.find_element(By.NAME, "dotransport").click()
        except:
            print("driver.find_element(By.NAME, dotransport).click() went wrong")
        time.sleep(sleepRandomLow() / 3)
        # TRY CATCH/EXCEPT IN CASE OF ERROR
        try:
            driver.find_element(By.NAME, "doTransport_confirm").click()
        except:
            print("driver.find_element(By.NAME, doTransport_confirm).click() went wrong")


def sendCarSpesificCity(driver):
    time.sleep(sleepRandomLow()/4)
    # Click sending car
    try:
        driver.find_element(By.XPATH, "//tr[@style='background-color: #ff4c4c;']").click()
    except:
        print("driver.find_element(By.XPATH, //tr[@style='background-color: #ff4c4c;']).click() went wrong")
    time.sleep(sleepRandomLow() / 4)
    # TRY CATCH/EXCEPT IN CASE OF ERROR
    try:
        select = Select(driver.find_element(By.NAME, "targetcity"))
        time.sleep(sleepRandomLow() / 4)
        select.select_by_value("5")
    except:
        print("select = Select(driver.find_element(By.NAME, targetcity)) went wrong")
    # actually send car
    time.sleep(sleepRandomLow() / 3)
    # TRY CATCH/EXCEPT IN CASE OF ERROR
    try:
        driver.find_element(By.NAME, "dotransport").click()
    except:
        print("driver.find_element(By.NAME, dotransport).click() went wrong")
    time.sleep(sleepRandomLow() / 3)
    # TRY CATCH/EXCEPT IN CASE OF ERROR
    try:
        driver.find_element(By.NAME, "doTransport_confirm").click()
    except:
        print("driver.find_element(By.NAME, doTransport_confirm).click() went wrong")


def sellCar(driver):
    try:
        elems = driver.find_elements(By.CSS_SELECTOR, "table.def_table.cursor>tbody>tr")
        carElems = []
        for i in elems:
            if not i.get_attribute("name") == "hlrow_table_select_gtaaction":
                carElems.append(i)

        for c in carElems:
            if c.get_attribute("style") == "background-color: #ff4c4c;" or c.get_attribute("style") == "background-color: rgb(255, 76, 76);":
                clickElem = c.find_element(By.CSS_SELECTOR, "td")
                clickElem.click()
                driver.find_element(By.NAME, "doSell").click()
            else:
                pass
    except:
        print("Cant sell cars")


def utforBiltyveri(driver, biltyveriAction):
    AntiBot.checkAntiBot(driver)
    # CHECK IF COUNTING
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        time.sleep(sleepRandomLow() / 2)
        # CHECK what action to do
        if biltyveriAction == 0:
            # DO RANDOM STUFF
            DoRandomStuff.doRandomStuff(driver)
            # SLEEP 5-10 SECONDS
            time.sleep(random.randint(5, 10))
        elif biltyveriAction == 1:
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                driver.find_element(By.ID, "rowid_table_select_gtaaction0").click()
            except:
                print("driver.find_element(By.ID, rowid_table_select_gtaaction0).click() went wrong")
        elif biltyveriAction == 2:
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                driver.find_element(By.ID, "rowid_table_select_gtaaction1").click()
            except:
                print("driver.find_element(By.ID, rowid_table_select_gtaaction1).click() went wrong")
        elif biltyveriAction == 3:
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                driver.find_element(By.ID, "rowid_table_select_gtaaction2").click()
            except:
                print("driver.find_element(By.ID, rowid_table_select_gtaaction2).click() went wrong")
        else:
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                driver.find_element(By.ID, "rowid_table_select_gtaaction3").click()
            except:
                print("driver.find_element(By.ID, rowid_table_select_gtaaction3).click() went wrong")
        # TRY CATCH/EXCEPT IN CASE OF ERROR
        try:
            biltyveriSuccess = driver.find_elements(By.CLASS_NAME, "successBox")
            if len(biltyveriSuccess) > 0:
                time.sleep(sleepRandomLow() / 2)
                # TRY TO SEND CAR AGAIN
                #sendCar(driver)
                carTR = driver.find_element(By.XPATH, "//tr[@style='background-color: #ff4c4c;']")
                carName = carTR.find_element(By.CSS_SELECTOR, "tr>td.carfield>div").get_attribute("innerHTML")
                carSkade = carTR.find_element(By.CSS_SELECTOR, "tr>td:nth-child(2)>div").get_attribute("innerHTML")
                if carName == "Mercedes-Benz SL 500" and GetCity.getCity(driver) == "Helsinki":
                    # sendCarSpesificCity(driver)
                    sellCar(driver)
                else:
                    if int(carSkade.replaceAll("%", "")) < 20:
                        sendCar(driver)
                    else:
                        sellCar(driver)
        except:
            print("biltyveriSuccess = driver.find_elements(By.CLASS_NAME, successBox) went wrong")
            #print("Retrying sending car")
            #sendCar(driver)
            carName = driver.find_element(By.XPATH, "//tr[@style='background-color: #ff4c4c;']")
            carName = carName.find_element(By.CSS_SELECTOR, "tr>td.carfield>div").get_attribute("innerHTML")
            if carName == "Mercedes-Benz SL 500" and GetCity.getCity(driver) == "Helsinki":
                #sendCarSpesificCity(driver)
                sellCar(driver)
            else:
                sellCar(driver)
    else:
        time.sleep(sleepRandomLow())
        print("Car timer is going")

def biltyveri(driver, biltyveriAction):
    IsLoggedIn.checkLogin(driver)
    # TRY CATCH/EXCEPT IN CASE OF ERROR
    try:
        driver.find_element(By.LINK_TEXT, "Biltyveri/Garasje").click()
    except:
        print("driver.find_element(By.LINK_TEXT, Biltyveri/Garasje).click() went wrong")
    if IsLoggedIn.checkLogin(driver):
        utforBiltyveri(driver, biltyveriAction)
    else:
        try:
            driver.find_element(By.LINK_TEXT, "Biltyveri/Garasje").click()
        except:
            print("driver.find_element(By.LINK_TEXT, Biltyveri/Garasje).click() went wrong 2")
        utforBiltyveri(driver, biltyveriAction)

