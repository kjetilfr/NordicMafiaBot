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
        AntiBot.checkAntiBot(driver)
        driver.find_element(By.NAME, "sellweed").click()
        driver.find_element(By.LINK_TEXT, "klikk her").click()
        driver.find_element(By.NAME, "transfermoney").click()
        BedriftsBank.withdrawAll(driver)
        Bank.bankIdealAmount(driver)
    except:
        print("Kunne ikke selge hasj")


def getArbeiderAndKvm(driver):
    try:
        AntiBot.checkAntiBot(driver)
        time.sleep(sleepRandomLow() / 3)
        currentMoney = GetMoney.getMoney(driver)
        spendingMoney = currentMoney
        ratioArbeider = 17600 * 2
        ratioKvm = 43500
        totRatio = ratioArbeider + ratioKvm
        devidedMoney = spendingMoney / totRatio
        arbeidererKjop = devidedMoney * ratioArbeider
        kvmKjop = devidedMoney * ratioKvm
        arbeidererKjop = int(arbeidererKjop)
        ratioArbeider = int(ratioArbeider)
        kvmKjop = int(kvmKjop)
        ratioKvm = int(ratioKvm)
        if (int(arbeidererKjop / ratioArbeider * 2)) % 2 == 0:
            investment = int(arbeidererKjop / ratioArbeider * 2)
        else:
            investment = int(arbeidererKjop / ratioArbeider * 2) - 1
        return investment, investment / 2
    except:
        print("Cant get Arbeider & Kvm")
        return 0, 0


def is_hasj_correct(driver):
    try:
        AntiBot.checkAntiBot(driver)
        hasj_table = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "weedFarmGeneralInfo")))
        kvm = hasj_table.find_element(By.CSS_SELECTOR, "tbody>tr>td:nth-child(2)").get_attribute("innerHTML")
        kvm = kvm[:-3]
        arb = hasj_table.find_element(By.CSS_SELECTOR, "tbody>tr:nth-child(2)>td:nth-child(2)").get_attribute("innerHTML")
        kvm = int(kvm)
        arb = int(arb)
        if kvm * 2 == arb:
            print("correct hasj ratio")
            return True
        else:
            return False
    except:
        print("Cant is hasj correct")


def fix_hasj(driver):
    try:
        AntiBot.checkAntiBot(driver)
        hasj_table = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "weedFarmGeneralInfo")))
        kvm = hasj_table.find_element(By.CSS_SELECTOR, "tbody>tr>td:nth-child(2)").get_attribute("innerHTML")
        kvm = kvm[:-3]
        arb = hasj_table.find_element(By.CSS_SELECTOR, "tbody>tr:nth-child(2)>td:nth-child(2)").get_attribute("innerHTML")
        kvm = int(kvm)
        arb = int(arb)
        if arb / 2 < kvm:
            buy_arb = kvm * 2 - arb
            money_on_hand = int(GetMoney.getMoney(driver))
            kan_kjope_arb_max = int(money_on_hand / 17600)
            if buy_arb > kan_kjope_arb_max:
                # Har ikkje råd til å kjøpe alt enn trenger så kjøper max
                print("kjøper " + str(kan_kjope_arb_max) + " arb")
                ansettArbeidere(driver, kan_kjope_arb_max)
            else:
                # Kjøper det enn trenger
                print("kjøper " + str(buy_arb) + " arb")
                ansettArbeidere(driver, buy_arb)
        elif arb / 2 > kvm:
            buy_kvm = (kvm * 2 - arb) * -2
            money_on_hand = int(GetMoney.getMoney(driver))
            kan_kjope_kvm_max = int(money_on_hand / 43500)
            if buy_kvm > kan_kjope_kvm_max:
                # Har ikkje råd til å kjøpe alt enn trenger så kjøper max
                print("kjøper " + str(kan_kjope_kvm_max) + " kvm")
                ansettKvm(driver, kan_kjope_kvm_max)
            else:
                # Kjøper det enn trenger
                print("kjøper " + str(buy_kvm) + " kvm")
                ansettKvm(driver, buy_kvm)
        else:
            print("What is happening?!")
    except:
        print("Cant fix hasj")



def flyttArbeidere(driver):
    try:
        AntiBot.checkAntiBot(driver)
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
        AntiBot.checkAntiBot(driver)
        time.sleep(sleepRandomLow() / 10)
        driver.find_element(By.NAME, "upgrade").click()
        arbeiderField = driver.find_element(By.NAME, "numWorkers")
        time.sleep(sleepRandomLow() / 10)
        arbeiderField.send_keys(Keys.BACKSPACE)
        time.sleep(sleepRandomLow() / 10)
        arbeiderField.send_keys(int(amount))
        time.sleep(sleepRandomLow() / 10)
        elements = driver.find_elements(By.NAME, "upgrade")
        time.sleep(sleepRandomLow() / 10)
        elements[0].click()
        time.sleep(sleepRandomLow() / 10)
        driver.find_element(By.LINK_TEXT, "Klikk her").click()
        time.sleep(sleepRandomLow())
        print("Ansatt " + str(amount) + " arb")
        flyttArbeidere(driver)
    except:
        print("Failed ansett arbeidere i hasjplantasjen")


def ansettKvm(driver, amount):
    try:
        AntiBot.checkAntiBot(driver)
        driver.find_element(By.NAME, "upgrade").click()
        time.sleep(sleepRandomLow() / 10)
        kvmField = driver.find_element(By.NAME, "numKvm")
        time.sleep(sleepRandomLow() / 10)
        kvmField.send_keys(Keys.BACKSPACE)
        time.sleep(sleepRandomLow() / 10)
        kvmField.send_keys(int(amount))
        time.sleep(sleepRandomLow() / 10)
        elements = driver.find_elements(By.NAME, "upgrade")
        time.sleep(sleepRandomLow() / 10)
        elements[1].click()
        time.sleep(sleepRandomLow() / 10)
        driver.find_element(By.LINK_TEXT, "Klikk her").click()
        print("Kjøpt " + str(amount) + " kvm")
    except:
        print("Failed ansett arbeidere i hasjplantasjen")


def oppgraderHasj(driver):
    AntiBot.checkAntiBot(driver)
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        try:
            check_hasj = is_hasj_correct(driver)
            if not check_hasj:
                fix_hasj(driver)
            else:
                getStats = getArbeiderAndKvm(driver)
                antallArbeidere = getStats[0]
                antallKvm = getStats[1]
                time.sleep(sleepRandomLow() / 10)
                ansettArbeidere(driver, antallArbeidere)
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
