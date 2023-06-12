from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


def sleepRandomLow():
    return random.randint(1, 3)


def login(driver, username, password):
    # LOGIN START
    usernameField = driver.find_element(By.NAME, "username")
    usrname = username
    psswrd = password
    # randomize username input start
    rndNumber = random.randint(0, len(username))
    usrnamep1 = usrname[:rndNumber]
    usrnamep2 = usrname[rndNumber:]
    usernameField.send_keys(usrnamep1)
    time.sleep(sleepRandomLow() / 10)
    usernameField.send_keys(usrnamep2)
    # randomize username input end
    passwordField = driver.find_element(By.NAME, "password")
    # randomize password input start
    rndNumber = random.randint(0, len(password))
    psswrdp1 = psswrd[:rndNumber]
    psswrdp2 = psswrd[rndNumber:]
    passwordField.send_keys(psswrdp1)
    time.sleep(sleepRandomLow() / 10)
    passwordField.send_keys(psswrdp2)
    # randomize password input end
    time.sleep(0.3)
    passwordField.send_keys(Keys.RETURN)
    # LOGIN END