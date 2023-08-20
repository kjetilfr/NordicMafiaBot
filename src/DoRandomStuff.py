from selenium.webdriver.common.by import By
import time
import random
from . import SleepRandom
from . import IsLoggedIn
from . import Sok


def doRandomStuff(driver):
    try:
        IsLoggedIn.checkLogin(driver)
        randomAction = random.randint(0, 5)
        if randomAction == 0:
            driver.find_element(By.LINK_TEXT, "Handlingslogg").click()
            #trykk på profila til den som hjeleper fra fengsel
            IsLoggedIn.checkLogin(driver)
            time.sleep(SleepRandom.sleepRandomLow() * 2)
        elif randomAction == 1:
            driver.find_element(By.LINK_TEXT, "Salg/Søknad forum").click()
            IsLoggedIn.checkLogin(driver)
            time.sleep(SleepRandom.sleepRandomLow() * 2)
            elements = driver.find_elements(By.XPATH, "//a[contains(@href, 'index.php?p=viewthread&tid=')]")
            randomPick = random.randint(0, 9)
            if elements[randomPick].text == "↑" or elements[randomPick].text == "Salg og søknad":
                # do nothing
                print("Do nothing")
            else:
                time.sleep(SleepRandom.sleepRandomLow())
                elements[randomPick].click()
        elif randomAction == 2:
            driver.find_element(By.LINK_TEXT, "Dagens mord").click()
            Sok.write_to_file_dead_players(Sok.dead_players(driver))
            IsLoggedIn.checkLogin(driver)
            time.sleep(SleepRandom.sleepRandomLow() * 2)
        elif randomAction == 3:
            driver.find_element(By.LINK_TEXT, "Innboks").click()
            IsLoggedIn.checkLogin(driver)
            time.sleep(SleepRandom.sleepRandomLow() * 2)
        elif randomAction == 4:
            # Gå til statetstikk og finn nye spillere
            Sok.write_to_file(Sok.new_players(driver))
        else:
            driver.find_element(By.LINK_TEXT, "Generelt forum").click()
            IsLoggedIn.checkLogin(driver)
            time.sleep(SleepRandom.sleepRandomLow() * 2)
    except:
        print("Cant do random event")
    time.sleep(5)
