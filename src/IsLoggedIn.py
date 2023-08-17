import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from . import Login


def checkLogin(driver):
    try:
        #Wait for load (1 second?) until element is located
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "usernameCont"))
            # This is a dummy element
        )
        username = elem.text
        #username = driver.find_element(By.ID, "usernameCont").text
        return True
    except:
        print("Not logged in, trying to login in 200 seconds")
        driver.get("http://www.nordicmafia.org")
        time.sleep(200)
        Login.login(driver)
        return False
