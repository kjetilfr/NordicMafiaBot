from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import random
import jsonRead
from src import *


settings = jsonRead.loadProfile()

test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

options = Options()
if settings["settings"][0]["Headless"] == 1:
    options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
    print("HEADLESS MODE (MIGHT NOT WORK OR MIGHT RESULT IN BAN! USE AT OWN RISK")

options.add_argument("--window-size=1920,1080")

options.add_argument(f'--user-agent={test_ua}')
# options.binary_location = "C:\Program Files\Google\Chrome Beta\Application"
chrome_driver_binary = "C:/chromedriver"
options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(chrome_driver_binary, options=options)
driver.get("http://www.nordicmafia.org")


def timeDown():
    sleepTime = random.randint(230, 280)
    print("Sleep " + str(sleepTime))
    time.sleep(sleepTime)


def doBotStuff():
    print("Start doBotStuff")
    timeDown()
    Bunker.gaaIBunkerCheck(driver)
    Kriminalitet.krim(driver, settings["settings"][2]["Kriminalitet"])
    Utpressing.utpress(driver, settings["settings"][2]["Utpressing"], settings["settings"][2]["UtpressingPerson"])
    FightClub.fightclub(driver, settings["settings"][2]["Fightclub"])
    Biltyveri.biltyveri(driver, settings["settings"][2]["Biltyveri"])
    Fengsel.fengsel(driver)
    doBotStuff()


def startBot():
    Login.login(driver, settings["settings"][1]["Brukernavn"], settings["settings"][1]["Passord"])
    Kriminalitet.krim(driver, settings["settings"][2]["Kriminalitet"])
    Utpressing.utpress(driver, settings["settings"][2]["Utpressing"], settings["settings"][2]["UtpressingPerson"])
    FightClub.fightclub(driver, settings["settings"][2]["Fightclub"])
    Biltyveri.biltyveri(driver, settings["settings"][2]["Biltyveri"])
    Bunker.gaaIBunkerCheck(driver)
    Fengsel.fengsel(driver)
    doBotStuff()


startBot()
