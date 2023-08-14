from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn
from . import DoRandomStuff
from . import GetMoney
from . import BedriftsBank
from . import Bank


def sleepRandomLow():
    return random.randint(1, 3)


def selgHasj(driver):
    try:
        driver.find_element(By.NAME, "sellweed").click()
        driver.find_element(By.LINK_TEXT, "klikk her").click()
        driver.find_element(By.NAME, "transfermoney").click()
        BedriftsBank.withdrawAll(driver)
        Bank.bankIdealAmount(driver)
    except:
        print("Kunne ikke selge hasj")


def getArbeiderAndKvm(driver):
    try:
        time.sleep(sleepRandomLow() / 3)
        currentMoney = GetMoney.getMoney(driver)
        spendingMoney = currentMoney
        ratioArbeider = 17600
        ratioKvm = 43500 * 2
        totRatio = ratioArbeider + ratioKvm
        devidedMoney = spendingMoney / totRatio
        arbeidererKjop = devidedMoney * ratioArbeider
        kvmKjop = devidedMoney * ratioKvm
        return int(arbeidererKjop / ratioArbeider), int(kvmKjop / ratioKvm * 2)
    except:
        print("Cant get Arbeider & Kvm")
        return 0, 0


def flyttArbeidere(driver):
    try:
        driver.find_element(By.NAME, "moveworkers").click()
        time.sleep(sleepRandomLow() / 10)
        arbeidsloseArbeidere = driver.find_element(By.CSS_SELECTOR, "table#weedFarmGeneralInfo>tbody>tr:nth-child(3)>td:nth-child(2)").get_attribute("innerHTML")
        time.sleep(sleepRandomLow() / 10)
        flyttField = driver.find_element(By.NAME, "numWorkers")
        time.sleep(sleepRandomLow() / 10)
        flyttField.send_keys(Keys.BACKSPACE)
        time.sleep(sleepRandomLow() / 10)
        flyttField.send_keys(arbeidsloseArbeidere)
        time.sleep(sleepRandomLow() / 10)
        driver.find_element(By.NAME, "moveworkers").click()
        time.sleep(sleepRandomLow() / 10)
        driver.find_element(By.LINK_TEXT, "Klikk her").click()
    except:
        print("Failed to move workers")


def ansettArbeidere(driver, amount):
    try:
        arbeiderField = driver.find_element(By.NAME, "numWorkers")
        time.sleep(sleepRandomLow() / 10)
        arbeiderField.send_keys(Keys.BACKSPACE)
        time.sleep(sleepRandomLow() / 10)
        arbeiderField.send_keys(amount)
        time.sleep(sleepRandomLow() / 10)
        elements = driver.find_elements(By.NAME, "upgrade")
        time.sleep(sleepRandomLow() / 10)
        elements[0].click()
        time.sleep(sleepRandomLow() / 10)
        driver.find_element(By.LINK_TEXT, "Klikk her").click()
        time.sleep(sleepRandomLow())
        flyttArbeidere(driver)
    except:
        print("Failed ansett arbeidere i hasjplantasjen")


def ansettKvm(driver, amount):
    try:
        kvmField = driver.find_element(By.NAME, "numKvm")
        time.sleep(sleepRandomLow() / 10)
        kvmField.send_keys(Keys.BACKSPACE)
        time.sleep(sleepRandomLow() / 10)
        kvmField.send_keys(amount)
        time.sleep(sleepRandomLow() / 10)
        elements = driver.find_elements(By.NAME, "upgrade")
        time.sleep(sleepRandomLow() / 10)
        elements[1].click()
        time.sleep(sleepRandomLow() / 10)
        driver.find_element(By.LINK_TEXT, "Klikk her").click()
    except:
        print("Failed ansett arbeidere i hasjplantasjen")


def oppgraderHasj(driver):
    AntiBot.checkAntiBot(driver)
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        try:
            getStats = getArbeiderAndKvm(driver)
            antallArbeidere = getStats[0]
            antallKvm = getStats[1]
            time.sleep(sleepRandomLow() / 10)
            driver.find_element(By.NAME, "upgrade").click()
            time.sleep(sleepRandomLow() / 10)
            ansettArbeidere(driver, antallArbeidere)
            time.sleep(sleepRandomLow() / 10)
            driver.find_element(By.NAME, "upgrade").click()
            ansettKvm(driver, antallKvm)
        except:
            print("Could not upgrade hasj")
    else:
        print("Hasj timer is going")


def hasj(driver):
    IsLoggedIn.checkLogin(driver)
    # Check if enough money to invest
    currentMoney = GetMoney.getMoney(driver)
    if currentMoney > 1200000:
        # invest in hp
        # TRY CATCH/EXCEPT IN CASE OF ERROR
        try:
            driver.find_element(By.LINK_TEXT, "Hasjplantasje").click()
            HasjMengde = driver.find_element(By.CSS_SELECTOR, "table#weedFarmGeneralInfo>tbody>tr:nth-child(5)>td:nth-child(2)")
            HashMengde = HasjMengde.get_attribute("innerHTML")
            if not HashMengde == "0 gram":
                selgHasj(driver)
        except:
            print("driver.find_element(By.LINK_TEXT, Hasjplantasje).click() went wrong")
        if IsLoggedIn.checkLogin(driver):
            oppgraderHasj(driver)
        else:
            try:
                driver.find_element(By.LINK_TEXT, "Hasjplantasje").click()
            except:
                print("driver.find_element(By.LINK_TEXT, Hasjplantasje).click() went wrong 2")
            oppgraderHasj(driver)
    else:
        # don't invest
        print("Below threshhold for investing in hp")
