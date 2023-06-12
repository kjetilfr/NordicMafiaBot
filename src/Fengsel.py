from selenium.webdriver.common.by import By
import time
import random
from . import DoRandomStuff
from . import AntiBot
from . import CheckCountdown
from . import SleepRandom
from . import IsLoggedIn


def sleepRandomLow():
    return random.randint(1, 3)


def brytUt(driver):
    AntiBot.checkAntiBot(driver)
    isCounting = CheckCountdown.checkCountdown(driver)
    # CHECK IF COUNTING
    if not isCounting:
        time.sleep(sleepRandomLow() / 2)
        # TRY CATCH/EXCEPT IN CASE OF ERROR
        try:
            antallPersonerSomKanBrytestUt = driver.find_elements(By.LINK_TEXT, "Bryt ut")
        except:
            print("driver.find_elements(By.LINK_TEXT, Bryt ut) went wrong")
        if len(antallPersonerSomKanBrytestUt) > 0:
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                driver.find_element(By.LINK_TEXT, "DUSØR").click()
            except:
                print("driver.find_elements(By.LINK_TEXT, Dusør) went wrong")
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                driver.find_element(By.LINK_TEXT, "Bryt ut").click()
            except:
                print("driver.find_elements(By.LINK_TEXT, Bryt ut) went wrong")
            time.sleep(SleepRandom.sleepRandomLow() + 2)
            isCounting = CheckCountdown.checkCountdown(driver)
            if not isCounting:
                brytUt(driver)
            else:
                time.sleep(SleepRandom.sleepRandomLow() + 1)
                print("Fengsel timer is going")
        else:
            time.sleep(random.randint(1, 2))
        if random.randint(1, 3) == 2:
            DoRandomStuff.doRandomStuff(driver)
    else:
        print("Fengsel timer is going")


def fengsel(driver):
    IsLoggedIn.checkLogin(driver)
    # TRY CATCH/EXCEPT IN CASE OF ERROR
    try:
        driver.find_element(By.LINK_TEXT, "Fengsel").click()
    except:
        print("driver.find_element(By.LINK_TEXT, Fengsel).click() went wrong")
    if IsLoggedIn.checkLogin(driver):
        brytUt(driver)
    else:
        # TRY CATCH/EXCEPT IN CASE OF ERROR
        try:
            driver.find_element(By.LINK_TEXT, "Fengsel").click()
        except:
            print("driver.find_element(By.LINK_TEXT, Fengsel).click() went wrong 2")
        brytUt(driver)
