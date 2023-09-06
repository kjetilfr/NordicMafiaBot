import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from . import Login
from Settings import jsonRead


def getData():
    data = jsonRead.smallLoad()
    return data

def checkLogin(driver):
    data = getData()
    try:
        #Wait for load (1 second?) until element is located
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "usernameCont"))
            # This is a dummy element
        )

        if elem.find_element(By.TAG_NAME, "a").get_attribute("innerHTML").lower() == data[1]["Brukernavn"].lower():
            return True
        else:
            print("Not logged in, trying to login in 60 seconds")
            driver.get("https://nordicmafia.org")
            time.sleep(60)
            Login.login(driver)
            return False
    except:
        print("Not logged in, trying to login in 60 seconds")
        driver.get("https://nordicmafia.org")
        time.sleep(60)
        Login.login(driver)
        return False
