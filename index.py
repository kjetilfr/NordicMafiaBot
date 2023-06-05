
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
from config.Login import login
from config.Biltyveri import biltyveri
from config.Utpressing import utpress
from config.Kriminalitet import krim
from config.Fengsel import fengsel
from config.FightClub import fightclub

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


def sleepRandomLow():
    return random.randint(1, 3)


def timeDown():
    x = 0
    while x < 10:
        sleepTime = random.randint(10, 50)
        time.sleep(sleepTime)
        print("Sleep " + str(sleepTime) + " " + str(x))
        x += 1


def doBotStuff():
    print("Start doBotStuff")
    timeDown()
    krim()
    fightclub()
    utpress()
    biltyveri()
    fengsel()
    doBotStuff()





def startBot():
    login(driver)
    krim(driver)
    fightclub(driver)
    utpress(driver)
    biltyveri(driver)
    fengsel(driver)
    doBotStuff(driver)


startBot()