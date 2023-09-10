from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn
from . import DoRandomStuff
from Settings import jsonRead


def sleepRandomLow():
    return random.randint(1, 3)


def getData():
    data = jsonRead.smallLoad()
    return data

def find_match(win_loss, kamp_matches):
    i = 0
    for a in kamp_matches:
        i += 1
        if i % 2 == 0:
            if win_loss == a.find_element(By.CSS_SELECTOR, "td:nth-child(3)").get_attribute("innerHTML"):
                return True
    return False

def check_fight(driver):
    try:
        data = getData()
        bet_amount = data[2]["Fightclub_belop"]
        # All matches available
        kamp_table = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.fightclub_box.fightclub_box-Kamper>table")))
        kamp_matches = kamp_table.find_elements(By.CSS_SELECTOR, "tr")

        # Personal info
        form_3 = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "form:nth-child(6)")))
        start_kamp_table = form_3.find_element(By.CSS_SELECTOR, "div.fightclub_box>table")
        win_loss = start_kamp_table.find_element(By.CSS_SELECTOR, "tr:nth-child(2)>td:nth-child(2)>span").get_attribute("innerHTML")
        time.sleep(0.5)
        if not find_match(win_loss, kamp_matches):
            belop_field = driver.find_element(By.NAME, "belop")
            belop_field.send_keys(bet_amount)
            time.sleep(0.3)
            driver.find_element(By.NAME, "startFight").click()
    except:
        print("Cant check fight")


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
    data = getData()
    IsLoggedIn.checkLogin(driver)
    # TRY CATCH/EXCEPT IN CASE OF ERROR
    try:
        driver.find_element(By.LINK_TEXT, "Fightclub").click()
    except:
        print("driver.find_element(By.LINK_TEXT, Fightclub).click() went wrong")
    if IsLoggedIn.checkLogin(driver):
        utforFightClub(driver, fightclubAction)
        if data[2]["Fightclub_fight"] == 1:
            check_fight(driver)
    else:
        # TRY CATCH/EXCEPT IN CASE OF ERROR
        try:
            driver.find_element(By.LINK_TEXT, "Fightclub").click()
        except:
            print("driver.find_element(By.LINK_TEXT, Fightclub).click() went wrong 2")
        utforFightClub(driver, fightclubAction)
