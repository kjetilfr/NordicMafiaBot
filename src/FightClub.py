from selenium.webdriver.common.by import By
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn
from . import DoRandomStuff


def sleepRandomLow():
    return random.randint(1, 3)


def utforFightClub(driver, fightclubAction):
    AntiBot.checkAntiBot(driver)
    # CHECK IF COUNTING
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        # FIGHTCLUB START
        time.sleep(sleepRandomLow() / 3)
        if fightclubAction == 0:
            # DO RANDOM STUFF
            DoRandomStuff.doRandomStuff(driver)
            # SLEEP 5-10 SECONDS
            time.sleep(random.randint(5, 10))
        elif fightclubAction == 1:
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                driver.find_element(By.XPATH, "//td[text()='11 pullups']").click()
            except:
                print("Fightclub action went wrong")
        elif fightclubAction == 2:
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                driver.find_element(By.XPATH, "//td[text()='5 benkpress']").click()
            except:
                print("Fightclub action went wrong")
        else:
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                driver.find_element(By.XPATH, "//td[text()='25 pushups']").click()
            except:
                print("Fightclub action went wrong")
    else:
        print("Fightclub timer is going")


def fightclub(driver, fightclubAction):
    IsLoggedIn.checkLogin(driver)
    # TRY CATCH/EXCEPT IN CASE OF ERROR
    try:
        driver.find_element(By.LINK_TEXT, "Fightclub").click()
    except:
        print("driver.find_element(By.LINK_TEXT, Fightclub).click() went wrong")
    if IsLoggedIn.checkLogin(driver):
        utforFightClub(driver, fightclubAction)
    else:
        # TRY CATCH/EXCEPT IN CASE OF ERROR
        try:
            driver.find_element(By.LINK_TEXT, "Fightclub").click()
        except:
            print("driver.find_element(By.LINK_TEXT, Fightclub).click() went wrong 2")
        utforFightClub(driver, fightclubAction)
