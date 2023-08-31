import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from . import GetMoney


def getBankValue(driver):
    try:
        if not driver.current_url == "https://nordicmafia.org/index.php?p=bank" or driver.current_url == "https://www.nordicmafia.org/index.php?p=bank":
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Bank"))).click()
        time.sleep(0.5)
        bankValue = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody>tr:nth-child(3)>td:nth-child(2)>span"))).get_attribute("innerHTML")
        bankValueWithComma = str(bankValue)[:-3]
        bankValueINT = int(bankValueWithComma.replace(",", ""))
        return bankValueINT
    except:
        print("Failed getBankValue")
        return 50000000


def depositXAmount(driver, amount):
    try:
        if not driver.current_url == "https://nordicmafia.org/index.php?p=bank" or driver.current_url == "https://www.nordicmafia.org/index.php?p=bank":
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Bank"))).click()
        time.sleep(0.5)
        belopField = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "depositAmount")))
        belopField.send_keys(amount)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "depositSingle"))).click()
    except:
        print("Failed deposit X")


def withdrawXAmount(driver, amount):
    try:
        if not driver.current_url == "https://nordicmafia.org/index.php?p=bank" or driver.current_url == "https://www.nordicmafia.org/index.php?p=bank":
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Bank"))).click()
        time.sleep(0.5)
        belopField = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "withdrawAmount")))
        belopField.send_keys(amount)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "withdrawSingle"))).click()
    except:
        print("Failed Withdraw X")

def withdrawAll(driver):
    try:
        if not driver.current_url == "https://nordicmafia.org/index.php?p=bank" or driver.current_url == "https://www.nordicmafia.org/index.php?p=bank":
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Bank"))).click()
        time.sleep(0.5)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "withdrawAll"))).click()
        return True
    except:
        print("Failed ta ut")
        return False


def depositAll(driver):
    try:
        time.sleep(0.4)
        if not driver.current_url == "https://nordicmafia.org/index.php?p=bank" or driver.current_url == "https://www.nordicmafia.org/index.php?p=bank":
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Bank"))).click()
        time.sleep(0.5)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "depositAll"))).click()
        return True
    except:
        print("Failed sett inn")
        return False


def bankIdealAmount(driver):
    try:
        if not driver.current_url == "https://nordicmafia.org/index.php?p=bank" or driver.current_url == "https://www.nordicmafia.org/index.php?p=bank":
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Bank"))).click()
        time.sleep(0.5)
        if getBankValue(driver) > 500000000:
            withdrawXAmount(driver, getBankValue(driver) - 500000000)
        time.sleep(0.5)
        bankValueWant = 500000000
        moneyOnHandWant = 200000
        if GetMoney.getMoney(driver) > 1200000:
            if getBankValue(driver) < bankValueWant:
                depositWant = bankValueWant - getBankValue(driver)
                wallet = GetMoney.getMoney(driver)
                depositMax = wallet - moneyOnHandWant
                if depositMax < depositWant:
                    depositXAmount(driver, depositMax)
                else:
                    depositXAmount(driver, depositWant)

    except:
        print("Could not bank ideal amount of money")
