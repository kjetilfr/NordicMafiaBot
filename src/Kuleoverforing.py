import random
from Settings import jsonRead
from selenium.webdriver.common.by import By
import time
from . import GetMoney


def getData():
    data = jsonRead.smallLoad()
    return data


def overfor1Kule(driver, person, price):
    try:
        driver.find_element(By.LINK_TEXT, "Overfør kuler").click()
        time.sleep(0.5)
        userField = driver.find_element(By.NAME, "transferUsername")
        userField.send_keys(person)
        bulletsField = driver.find_element(By.NAME, "transferBullets")
        bulletsField.send_keys("1")
        priceField = driver.find_element(By.NAME, "transferPrice")
        priceField.send_keys(price)
        passwordField = driver.find_element(By.NAME, "transferPassword")
        data = getData()
        passwordField.send_keys(data[1]["Passord"])
        driver.find_element(By.NAME, "startTransfer").click()
    except:
        print("Failed deposit X")


def overforXKuler(driver, bullets, person, price):
    try:
        driver.find_element(By.LINK_TEXT, "Overfør kuler").click()
        time.sleep(0.5)
        userField = driver.find_element(By.NAME, "transferUsername")
        userField.send_keys(person)
        bulletsField = driver.find_element(By.NAME, "transferBullets")
        bulletsField.send_keys(bullets)
        priceField = driver.find_element(By.NAME, "transferPrice")
        priceField.send_keys(price)
        passwordField = driver.find_element(By.NAME, "transferPassword")
        data = getData()
        passwordField.send_keys(data[1]["Passord"])
        driver.find_element(By.NAME, "startTransfer").click()
    except:
        print("Failed deposit X")
