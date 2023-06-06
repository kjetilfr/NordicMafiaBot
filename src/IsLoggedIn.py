import time
from selenium.webdriver.common.by import By
from . import Login


def checkLogin(driver):
    try:
        username = driver.find_element(By.ID, "usernameCont").text
        print("Logged in as " + username)
    except:
        print("Not logged in")
        driver.get("http://www.nordicmafia.org")
        time.sleep(500)
        Login.login(driver)
