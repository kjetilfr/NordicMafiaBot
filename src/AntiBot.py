from selenium.webdriver.common.by import By
from src import IsLoggedIn
from . import byeAllCaptcha



def checkAntiBot(driver):
    try:
        #IsLoggedIn.checkLogin(driver)
        if len(driver.find_elements(By.XPATH, "//div[text()='Anti-bot']")) > 0 or len(driver.find_elements(By.CLASS_NAME, "g-recaptcha")) > 0:
            byeAllCaptcha.solve_recaptcha(driver)
        else:
            print("no bot")
    except:
        pass

