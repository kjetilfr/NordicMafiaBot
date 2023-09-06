from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn


def check_rich(driver):
    rich_list = [["Troublesome", 3072], ["Bartzabel", 3115], ["Erna Solberg", 295], ["Ice Cold", 28], ["Toxic", 892], ["Crazyeye", 865], ["Waaler", 742], ["John Gotti", 223]]
    pre_link = "https://nordicmafia.org/index.php?p=profile&id="
    i = 0
    while i < len(rich_list):
        if not IsLoggedIn.checkLogin(driver):
            break
        try:
            driver.get(pre_link + str(rich_list[i][1]))
            time.sleep(1)
            table = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table>tbody")))
            pengestatus = table.find_element(By.CSS_SELECTOR, "tr:nth-child(7)>td:nth-child(2)")
            pengestatus = pengestatus.get_attribute("innerHTML")
            if pengestatus == "Beryktende rik":
                time.sleep(1)
                driver.find_element(By.LINK_TEXT, "Utpressing").click()
                return rich_list[i][0]
        except:
            print("failed check_rich")
        time.sleep(2)
        i += 1
    time.sleep(1)
    try:
        driver.find_element(By.LINK_TEXT, "Utpressing").click()
    except:
        print("failed to click utpressing")
    return "Bartzabel"


def sleepRandomLow():
    return random.randint(1, 3)


def utforUtpress(driver, utpressAction, utpressPerson):
    AntiBot.checkAntiBot(driver)
    # CHECK TIMER
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        time.sleep(sleepRandomLow() / 3)
        # CHECK UTPRESS ACTION
        if utpressAction == 1:
            # UTPRESS SPESIFIC PERSON
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                driver.find_element(By.ID, "sel_2").click()
            except:
                print("driver.find_element(By.ID, sel_2).click() went wrong")
            # SKRIV INN SPILLERS NAVN
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                # GET FIELD
                personField = driver.find_element(By.NAME, "blackmailUser")
                # SEND KEYS
                personField.send_keys(utpressPerson)
            except:
                print("driver.find_element(By.NAME, blackmailUser) or sendkeys went wrong")
            time.sleep(sleepRandomLow() / 3)
            # UTFØR UTPRESSING
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                driver.find_element(By.NAME, "submitBlackmail").click()
            except:
                print("driver.find_element(By.NAME, submitBlackmail).click() went wrong")
        else:
            # UTPRESS TILFELDIG PERSON
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                driver.find_element(By.ID, "sel_1").click()
            except:
                print("driver.find_element(By.ID, sel_1).click() went wrong")
            time.sleep(sleepRandomLow() / 3)
            # UTFØR UTPRESSING
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                driver.find_element(By.NAME, "submitBlackmail").click()
            except:
                print("driver.find_element(By.NAME, submitBlackmail).click() went wrong")
    else:
        print("Utpress timer is going")


def utpress(driver, utpressAction, utpressPerson):
    IsLoggedIn.checkLogin(driver)
    try:
        driver.find_element(By.LINK_TEXT, "Utpressing").click()
    except:
        print("driver.find_element(By.LINK_TEXT, Utpressing).click() went wrong")
    if IsLoggedIn.checkLogin(driver):
        new = 0
        if new == 1:
            utforUtpress(driver, 1, check_rich(driver))
        else:
            utforUtpress(driver, utpressAction, utpressPerson)
    else:
        try:
            driver.find_element(By.LINK_TEXT, "Utpressing").click()
        except:
            print("driver.find_element(By.LINK_TEXT, Utpressing).click() went wrong 2")
        utforUtpress(driver, utpressAction, utpressPerson)
