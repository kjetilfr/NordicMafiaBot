from selenium.webdriver.common.by import By


def getCity(driver):
    whereIsPlayer = driver.find_elements(By.CLASS_NAME, "value")
    fullWhere = whereIsPlayer[1].get_attribute("outerHTML")
    city = fullWhere[20:]
    city = city[:-7]
    return city