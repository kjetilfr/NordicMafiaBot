from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import random
from Settings import jsonRead
from src import GetCity, AntiBot, Biltyveri, Bunker, CheckCountdown, DoRandomStuff, Fengsel, FightClub, GetTime, IsLoggedIn, Kriminalitet, Login, LongBreak, SleepRandom, Utpressing
from selenium.webdriver.common.by import By
import time
import datetime
import random


def getBankValue(driver):
    try:
        driver.find_element(By.LINK_TEXT, "Bedriftsbanken").click()
        bankValue = driver.find_element(By.CSS_SELECTOR, "tbody>tr:nth-child(2)>td.right").get_attribute("innerHTML")
        bankValueWithComma = str(bankValue)[:-3]
        bankValueINT = int(bankValueWithComma.replace(",", ""))
        return bankValueINT
    except:
        print("Failed getBankValue")
        return 0


def depositXAmount(driver, amount):
    try:
        driver.find_element(By.LINK_TEXT, "Bedriftsbanken").click()
        time.sleep(0.5)
        belopField = driver.find_element(By.NAME, "settinn_belop")
        driver.find_element(By.NAME, "settinn_mode").click()
        belopField.send_keys(Keys.BACKSPACE)
        belopField.send_keys(amount)
        driver.find_element(By.NAME, "settinn").click()
    except:
        print("Failed deposit X")


def withdrawXAmount(driver, amount):
    try:
        driver.find_element(By.LINK_TEXT, "Bedriftsbanken").click()
        time.sleep(0.5)
        belopField = driver.find_element(By.NAME, "taut_belop")
        driver.find_element(By.NAME, "taut_mode").click()
        belopField.send_keys(Keys.BACKSPACE)
        belopField.send_keys(amount)
        driver.find_element(By.NAME, "taut").click()
    except:
        print("Failed Withdraw X")


def withdrawAll(driver):
    try:
        driver.find_element(By.LINK_TEXT, "Bedriftsbanken").click()
        time.sleep(0.5)
        driver.find_element(By.NAME, "taut").click()
        return True
    except:
        print("Failed ta ut")
        return False


def depositAll(driver):
    try:
        driver.find_element(By.LINK_TEXT, "Bedriftsbanken").click()
        time.sleep(0.5)
        driver.find_element(By.NAME, "settinn").click()
        return True
    except:
        print("Failed sett inn")
        return False