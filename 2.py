from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import random
from Settings import jsonRead
from src import *
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ua = UserAgent()
user_agent = ua.random
options = webdriver.FirefoxOptions()


options.add_argument("--window-size=1920,1080")

chrome_driver_binary = "C:/chromedriver"
options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")
options.add_argument(f'--user-agent={user_agent}')
options.set_preference('intl.accept_languages', 'en-GB')

driver = webdriver.Firefox(options=options)
#driver.get("https://www.google.com/recaptcha/api2/demo")
driver.get("file:///C:/Users/Kjetil/Desktop/3.htm")
# driver.get("https://nordicmafia.org")


def sleepRandomLow():
    return random.randint(1, 3)


def check_fight(driver):
    # All matches available
    kamp_table = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.fightclub_box.fightclub_box-Kamper>table")))
    kamp_matches = kamp_table.find_elements(By.CSS_SELECTOR, "tr")

    # Personal info
    form_3 = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "form:nth-child(5)")))
    start_kamp_table = WebDriverWait(form_3, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.fightclub_box>table")))
    win_loss = start_kamp_table.find_element(By.CSS_SELECTOR, "tr:nth-child(2)>td:nth-child(2)>span").get_attribute("innerHTML")

    for a in enumerate(kamp_matches):

        print(a.find_element(By.CSS_SELECTOR, "td:nth-child(3)").get_attribute("innerHTML"))

    # profile_name = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "bullets")))


check_fight(driver)

time.sleep(20000)
