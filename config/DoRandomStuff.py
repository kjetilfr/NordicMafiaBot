from selenium.webdriver.common.by import By
import time
import random
from SleepRandomLow import sleepRandomLow


def doRandomStuff(driver):
    randomAction = random.randint(0, 4)
    print(randomAction)
    if randomAction == 0:
        driver.find_element(By.LINK_TEXT, "Handlingslogg").click()
        time.sleep(sleepRandomLow() * 2)
        print("Hey")
    elif randomAction == 1:
        print("111")
        driver.find_element(By.LINK_TEXT, "Salg/Søknad forum").click()
        time.sleep(sleepRandomLow() * 2)
        elements = driver.find_elements(By.XPATH, "//a[contains(@href, 'index.php?p=viewthread&tid=')]")
        print(elements)
        print(elements[0])
        for element in elements:
            print(element.text)
        randomPick = random.randint(0, 9)
        if elements[randomPick].text == "↑" or elements[randomPick].text == "Salg og søknad":
            #do nothing
            print(elements[randomPick].text + " ↑")
        else:
            time.sleep(sleepRandomLow())
            print(elements[randomPick].text)
            elements[randomPick].click()
    elif randomAction == 2:
        print("2222")
        driver.find_element(By.LINK_TEXT, "Dagens mord").click()
        time.sleep(sleepRandomLow() * 2)
    elif randomAction == 3:
        print("333333")
        driver.find_element(By.LINK_TEXT, "Innboks").click()
        time.sleep(sleepRandomLow() * 2)
    else:
        print("else")
        driver.find_element(By.LINK_TEXT, "Generelt forum").click()
        time.sleep(sleepRandomLow() * 2)
    time.sleep(5)
