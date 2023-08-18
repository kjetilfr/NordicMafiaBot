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


def brytUtPerson(driver):
    AntiBot.checkAntiBot(driver)
    isCounting = CheckCountdown.checkCountdown(driver)
    # CHECK IF COUNTING
    if not isCounting:
        try:
            # Prøver å bryte ut person som er oppdraget
            time.sleep(sleepRandomLow() / 2)
            oppdragPerson = driver.find_element(By.XPATH, "//tr[@style='background-color: #1A3A62;']")
            knapp = oppdragPerson.find_element(By.LINK_TEXT, "Bryt ut")
            knapp.click()
            extraSleepTime = 6 * 60
            print("Sleeping extra " + str(extraSleepTime) + " seconds")
            time.sleep(extraSleepTime)
        except:
            # TRY CATCH/EXCEPT IN CASE OF ERROR
            try:
                antallPersonerSomKanBrytestUt = driver.find_elements(By.LINK_TEXT, "Bryt ut")
            except:
                print("driver.find_elements(By.LINK_TEXT, Bryt ut) went wrong")
            if len(antallPersonerSomKanBrytestUt) > 0:
                # TRY CATCH/EXCEPT IN CASE OF ERROR
                # Prøver å bryte ut fra gjeng
                try:
                    everyoneInJail = driver.find_elements(By.CSS_SELECTOR,
                                                          "table.def_table.def_table_left.coloringTable>tbody>tr")
                    for test in everyoneInJail[1:]:
                        # Is person in gang
                        if len(test.find_elements(By.CSS_SELECTOR, "td>a>span")) > 0:
                            try:
                                brytUt = test.find_element(By.LINK_TEXT, "Bryt ut").get_attribute("innerHTML")
                                if brytUt == "Bryt ut":
                                    test.find_element(By.LINK_TEXT, "Bryt ut").click()
                                    break
                            except:
                                pass
                        else:
                            print("Ingen i gjeng å bryte ut")
                            try:
                                driver.find_element(By.LINK_TEXT, "DUSØR").click()
                            except:
                                print("driver.find_elements(By.LINK_TEXT, Dusør) went wrong")
                            # TRY CATCH/EXCEPT IN CASE OF ERROR
                            try:
                                isCounting = CheckCountdown.checkCountdown(driver)
                                if not isCounting:
                                    driver.find_element(By.LINK_TEXT, "Bryt ut").click()
                            except:
                                print("driver.find_elements(By.LINK_TEXT, Bryt ut) went wrong")
                        time.sleep(SleepRandom.sleepRandomLow() + 2)
                        isCounting = CheckCountdown.checkCountdown(driver)
                        if not isCounting:
                            pass
                        else:
                            time.sleep(SleepRandom.sleepRandomLow() + 1)
                            print("Fengsel timer is going")
                except:
                    print("Ingen i gjeng å bryte ut")
                    try:
                        driver.find_element(By.LINK_TEXT, "DUSØR").click()
                        time.sleep(0.2)
                    except:
                        print("driver.find_elements(By.LINK_TEXT, Dusør) went wrong")
                    # TRY CATCH/EXCEPT IN CASE OF ERROR
                    try:
                        isCounting = CheckCountdown.checkCountdown(driver)
                        if not isCounting:
                            driver.find_element(By.LINK_TEXT, "Bryt ut").click()
                    except:
                        print("driver.find_elements(By.LINK_TEXT, Bryt ut) went wrong")
                time.sleep(SleepRandom.sleepRandomLow() + 2)
                isCounting = CheckCountdown.checkCountdown(driver)
                if not isCounting:
                    brytUtPerson(driver)
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
        brytUtPerson(driver)
    else:
        # TRY CATCH/EXCEPT IN CASE OF ERROR
        try:
            driver.find_element(By.LINK_TEXT, "Fengsel").click()
        except:
            print("driver.find_element(By.LINK_TEXT, Fengsel).click() went wrong 2")
        brytUtPerson(driver)
