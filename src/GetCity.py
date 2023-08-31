import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getCity(driver):
    try:
        time.sleep(0.5)
        whereIsPlayer = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "value")))
        fullWhere = whereIsPlayer[1].get_attribute("outerHTML")
        city = fullWhere[20:]
        city = city[:-7]
        return city
    except:
        print("could not get city sending Helsinki")
        return "Helsinki"
