from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


def sleepRandomLow():
    return random.randint(1, 3)


def getConfig():
    myConfig = dict()
    fh = open('foobar.config').readlines()
    for line in fh:
        row = line.split(',')
    myConfig['username'] = row[0]
    myConfig['password'] = row[1]
    return myConfig

#print(getConfig())


def login(driver):
    myDetails = getConfig()
    # LOGIN START
    username = driver.find_element(By.NAME, "username")
    usrname = myDetails['username']
    psswrd = myDetails['password']
    # randomize username input start
    rndNumber = random.randint(0, len(myDetails['username']))
    usrnamep1 = usrname[:rndNumber]
    usrnamep2 = usrname[rndNumber:]
    username.send_keys(usrnamep1)
    time.sleep(sleepRandomLow() / 10)
    username.send_keys(usrnamep2)
    # randomize username input end
    password = driver.find_element(By.NAME, "password")
    # randomize password input start
    rndNumber = random.randint(0, len(myDetails['password']))
    psswrdp1 = psswrd[:rndNumber]
    psswrdp2 = psswrd[rndNumber:]
    password.send_keys(psswrdp1)
    time.sleep(sleepRandomLow() / 10)
    password.send_keys(psswrdp2)
    # randomize password input end
    time.sleep(0.3)
    password.send_keys(Keys.RETURN)
    # LOGIN END