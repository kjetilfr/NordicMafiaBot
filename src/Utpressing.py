from selenium.webdriver.common.by import By
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn


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
        utforUtpress(driver, utpressAction, utpressPerson)
    else:
        try:
            driver.find_element(By.LINK_TEXT, "Utpressing").click()
        except:
            print("driver.find_element(By.LINK_TEXT, Utpressing).click() went wrong 2")
        utforUtpress(driver, utpressAction, utpressPerson)
