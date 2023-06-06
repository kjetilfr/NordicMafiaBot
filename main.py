from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import random
from src import *


test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

options = Options()

# options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
options.add_argument("--window-size=1920,1080")

options.add_argument(f'--user-agent={test_ua}')
# options.binary_location = "C:\Program Files\Google\Chrome Beta\Application"
chrome_driver_binary = "C:/chromedriver"
options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(chrome_driver_binary, options=options)
driver.get("http://www.nordicmafia.org")

#test
#driver = webdriver.Chrome()
#driver.get('file:///C:/Users/Kjetil/Downloads/forum.html')


def timeDown():
    sleepTime = random.randint(180, 230)
    print("Sleep " + str(sleepTime))
    time.sleep(sleepTime)


def doBotStuff():
    print("Start doBotStuff")
    timeDown()
    Bunker.gaaIBunkerCheck(driver)
    Kriminalitet.krim(driver)
    FightClub.fightclub(driver)
    Utpressing.utpress(driver)
    Biltyveri.biltyveri(driver)
    Fengsel.fengsel(driver)
    doBotStuff()


def startBot():
    Login.login(driver)
    Kriminalitet.krim(driver)
    FightClub.fightclub(driver)
    Utpressing.utpress(driver)
    Biltyveri.biltyveri(driver)
    Bunker.gaaIBunkerCheck(driver)
    Fengsel.fengsel(driver)
    doBotStuff()


startBot()
