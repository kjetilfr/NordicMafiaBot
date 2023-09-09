from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn
from . import DoRandomStuff


def sleepRandomLow():
    return random.randint(1, 3)


def utforKrim(driver, krimAction):
    AntiBot.checkAntiBot(driver)
    isCounting = CheckCountdown.checkCountdown(driver)
    if isCounting == False:
        time.sleep(sleepRandomLow() / 3)
        try:
            # 10% Chance to do krimaction0 to increase chance of success
            oneinten = random.randint(1, 10)
            if oneinten != 10:
                if krimAction == 0:
                    # skip
                    DoRandomStuff.doRandomStuff(driver)
                    time.sleep(7)
                if krimAction == 1:
                    # TRY CATCH/EXCEPT IN CASE OF ERROR
                    try:
                        elem = WebDriverWait(driver, 0.5).until(
                            EC.presence_of_element_located((By.ID, "rowid_table_select_krimaction0"))  # This is a dummy element
                        )
                        elem.click()
                        #driver.find_element(By.ID, "rowid_table_select_krimaction0").click()
                    except:
                        print("driver.find_element(By.ID, rowid_table_select_krimaction0).click() went wrong")
                elif krimAction == 2:
                    # TRY CATCH/EXCEPT IN CASE OF ERROR
                    try:
                        elem = WebDriverWait(driver, 0.5).until(
                            EC.presence_of_element_located((By.ID, "rowid_table_select_krimaction1"))
                            # This is a dummy element
                        )
                        elem.click()
                        #driver.find_element(By.ID, "rowid_table_select_krimaction1").click()
                    except:
                        print("driver.find_element(By.ID, rowid_table_select_krimaction1).click() went wrong")
                elif krimAction == 3:
                    # TRY CATCH/EXCEPT IN CASE OF ERROR
                    try:
                        elem = WebDriverWait(driver, 0.5).until(
                            EC.presence_of_element_located((By.ID, "rowid_table_select_krimaction2"))
                            # This is a dummy element
                        )
                        elem.click()
                        #driver.find_element(By.ID, "rowid_table_select_krimaction2").click()
                    except:
                        print("driver.find_element(By.ID, rowid_table_select_krimaction2).click() went wrong")
                elif krimAction == 4:
                    # TRY CATCH/EXCEPT IN CASE OF ERROR
                    try:
                        elem = WebDriverWait(driver, 0.5).until(
                            EC.presence_of_element_located((By.ID, "rowid_table_select_krimaction3"))
                            # This is a dummy element
                        )
                        elem.click()
                        #driver.find_element(By.ID, "rowid_table_select_krimaction3").click()
                    except:
                        print("driver.find_element(By.ID, rowid_table_select_krimaction3).click() went wrong")
                else:
                    # TRY CATCH/EXCEPT IN CASE OF ERROR
                    try:
                        elem = WebDriverWait(driver, 0.5).until(
                            EC.presence_of_element_located((By.ID, "rowid_table_select_krimaction4"))
                            # This is a dummy element
                        )
                        elem.click()
                        #driver.find_element(By.ID, "rowid_table_select_krimaction4").click()
                    except:
                        print("driver.find_element(By.ID, rowid_table_select_krimaction4).click() went wrong")
            else:
                # TRY CATCH/EXCEPT IN CASE OF ERROR
                try:
                    driver.find_element(By.ID, "rowid_table_select_krimaction0").click()
                except:
                    print("driver.find_element(By.ID, rowid_table_select_krimaction0).click() went wrong")
        except:
            print("Krim went wrong")
    else:
        print("Krim timer is going")


def krim(driver, krimAction):
    IsLoggedIn.checkLogin(driver)
    # TRY CATCH/EXCEPT IN CASE OF ERROR
    try:
        driver.find_element(By.LINK_TEXT, "Kriminalitet").click()
    except:
        print("driver.find_element(By.LINK_TEXT, Kriminalitet).click() went wrong")
    if IsLoggedIn.checkLogin(driver):
        utforKrim(driver, krimAction)
    else:
        try:
            driver.find_element(By.LINK_TEXT, "Kriminalitet").click()
        except:
            print("driver.find_element(By.LINK_TEXT, Kriminalitet).click() went wrong 2")
        utforKrim(driver, krimAction)
