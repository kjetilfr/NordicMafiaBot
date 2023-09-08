from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from Settings import jsonRead
from . import IsLoggedIn


def getData():
    data = jsonRead.smallLoad()
    return data


def sleepRandomLow():
    return random.randint(1, 3)


def login(driver):
    try:
        data = getData()
        # LOGIN START
        usernameField = driver.find_element(By.NAME, "username")
        usrname = data[1]["Brukernavn"]
        print(usrname)
        psswrd = data[1]["Passord"]
        print(psswrd)
        # randomize username input start
        rndNumber = random.randint(0, len(usrname))
        usrnamep1 = usrname[:rndNumber]
        usrnamep2 = usrname[rndNumber:]
        usernameField.send_keys(usrnamep1)
        time.sleep(sleepRandomLow() / 10)
        usernameField.send_keys(usrnamep2)
        # randomize username input end
        passwordField = driver.find_element(By.NAME, "password")
        # randomize password input start
        rndNumber = random.randint(0, len(psswrd))
        psswrdp1 = psswrd[:rndNumber]
        psswrdp2 = psswrd[rndNumber:]
        passwordField.send_keys(psswrdp1)
        time.sleep(sleepRandomLow() / 10)
        passwordField.send_keys(psswrdp2)
        # randomize password input end
        time.sleep(0.3)
        passwordField.send_keys(Keys.RETURN)
        # LOGIN END
        IsLoggedIn.checkLogin(driver)
    except:
        print("Something went wrong with login")
