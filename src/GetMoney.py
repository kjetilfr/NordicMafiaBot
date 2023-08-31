from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from . import SleepRandom
import time

def getMoney(driver):
    try:
        time.sleep(SleepRandom.sleepRandomLow() / 2)
        amountOfMoney = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "money_hand")))
        fullMoney = amountOfMoney.get_attribute("innerHTML")
        money = fullMoney[6:]
        money = money[:-7]
        # make money an integer
        money = money.replace(",", "")
        money = int(money)
        return money
    except:
        print("Cant find money on hand, returning 0")
        return 0
