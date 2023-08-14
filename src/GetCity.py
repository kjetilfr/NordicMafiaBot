import time

from selenium.webdriver.common.by import By


def getCity(driver):
    try:
        time.sleep(0.5)
        whereIsPlayer = driver.find_elements(By.CLASS_NAME, "value")
        fullWhere = whereIsPlayer[1].get_attribute("outerHTML")
        city = fullWhere[20:]
        city = city[:-7]
        return city
    except:
        print("could not get city sending Helsinki")
        return "Helsinki"