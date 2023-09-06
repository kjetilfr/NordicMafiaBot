import time
from . import GetMoney
from selenium.webdriver.common.by import By
from . import IsLoggedIn
from . import GetTimer
from Settings import jsonRead
from . import Bank
from . import Kuleoverforing

def getData():
    data = jsonRead.smallLoad()
    return data


def rekrutterGangstere(driver, uts):
    totalUTS = uts
    if totalUTS > 99:
        utsUsed = 99
        driver.find_element(By.NAME, "numuts").send_keys(utsUsed)
        time.sleep(0.2)
        driver.find_element(By.NAME, "dorecruit").click()
        time.sleep(0.2)
        driver.find_element(By.LINK_TEXT, "Club dè Gangster").click()
    else:
        print("Out of UTS buy more or wait for regeneration")


def posisjonerGangstere(driver, uposisjonerteGangstere):
    try:
        driver.find_element(By.ID, "rowid_table_select_cdgaction2").click()
        time.sleep(0.2)
        driver.find_element(By.ID, "rowid_table_select_cdgselecttransferdirection0").click()
        time.sleep(0.2)
        antallFlyttesField = driver.find_element(By.NAME, "numgangsters")
        antallFlyttesField.send_keys(uposisjonerteGangstere)
        time.sleep(0.2)
        driver.find_element(By.NAME, "dotransfer").click()
    except:
        print("posisjon Error")


def CDGAngrip(driver, username, gangsters=1):
    try:
        time.sleep(1)
        uts = driver.find_element(By.CSS_SELECTOR, "table.cdg_table>tbody>tr:nth-child(1)>td:nth-child(2)")
        uts = uts.get_attribute("innerHTML")
        uts = uts.replace(",", "")
        uts = int(uts)
        uposisjonerteGangstere = driver.find_element(By.CSS_SELECTOR, "table.cdg_table>tbody>tr:nth-child(2)>td:nth-child(2)")
        uposisjonerteGangstere = int(uposisjonerteGangstere.get_attribute("innerHTML"))
        gangstereIAngrep = driver.find_element(By.CSS_SELECTOR, "table.cdg_table>tbody>tr:nth-child(4)>td:nth-child(2)")
        gangstereIAngrep = int(gangstereIAngrep.get_attribute("innerHTML"))
        if gangstereIAngrep > 1:
            driver.find_element(By.ID, "rowid_table_select_cdgaction0").click()
            time.sleep(0.2)
            sendGansterAmountField = driver.find_element(By.NAME, "numgangsters")
            sendGansterAmountField.send_keys(gangsters)
            time.sleep(0.2)
            victimField = driver.find_element(By.NAME, "victimname")
            victimField.send_keys(username)
            time.sleep(0.2)
            driver.find_element(By.NAME, "doattack").click()
        elif gangstereIAngrep == 0 and uposisjonerteGangstere > 0:
            time.sleep(0.2)
            posisjonerGangstere(driver, uposisjonerteGangstere)
        else:
            driver.find_element(By.ID, "rowid_table_select_cdgaction2").click()
            rekrutterGangstere(driver, uts)
            uposisjonerteGangstere = driver.find_element(By.CSS_SELECTOR, "table.cdg_table>tbody>tr:nth-child(2)>td:nth-child(2)")
            uposisjonerteGangstere = int(uposisjonerteGangstere.get_attribute("innerHTML"))
            time.sleep(0.2)
            posisjonerGangstere(driver, uposisjonerteGangstere)
            time.sleep(0.2)
    except:
        print("failed cdg attack")



def cdg(driver, username, gangsters):
    try:
        data = getData()
        Bank.depositAll(driver)
        driver.find_element(By.LINK_TEXT, "Club dè Gangster").click()
        if GetMoney.getMoney(driver) > 0:
            Bank.depositAll(driver)
            CDGAngrip(driver, username, gangsters)
        else:
            CDGAngrip(driver, username, gangsters)
        #Check if win or lose
        time.sleep(1)
        # if 14356 <= GetTimer.getTimer(driver, "Club dè gangster") <= 14600 and str(driver.find_element(By.CSS_SELECTOR, "div.defpadding>span:nth-child(2)").get_attribute("innerHTML")) == "mislykket":
            # Kuleoverforing.overfor1Kule(driver, data[2]["CDGPerson"], 40000000)
    except:
        print("driver.find_element(By.LINK_TEXT, Club dè Gangster).click() went wrong")
        if IsLoggedIn.checkLogin(driver):
            CDGAngrip(driver, username, gangsters)
        else:
            try:
                driver.find_element(By.LINK_TEXT, "Club dè Gangster").click()
            except:
                print("driver.find_element(By.LINK_TEXT, Club dè Gangster).click() went wrong 2")
            CDGAngrip(driver, username, gangsters)
