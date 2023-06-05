from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
import time
from SleepRandomLow import sleepRandomLow

def checkAntiBot(driver):
    if len(driver.find_elements(By.XPATH, "//div[text()='Anti-bot']")) > 0:
        print("bot")
        time.sleep(sleepRandomLow()/2)
        solver = RecaptchaSolver(driver=driver)
        recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
        try:
            solver.click_recaptcha_v2(iframe=recaptcha_iframe)
        except:
            driver.refresh()
            print("listening error captcha")
        else:
            driver.refresh()
            print("something else went wrong")
    else:
        print("no bot")