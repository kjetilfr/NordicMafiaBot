from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random

test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

options = Options()

# options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
options.add_argument("--window-size=1920,1080")

options.add_argument(f'--user-agent={test_ua}')
# options.binary_location = "C:\Program Files\Google\Chrome Beta\Application"
chrome_driver_binary = "C:/chromedriver"
options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(chrome_driver_binary, options=options)
driver.get("http://www.nordicmafia.org")
#driver.get('file:///C:/Users/Kjetil/Desktop/nm%20antibot.html')


def getConfig():
    myConfig = dict()
    fh = open('foobar.config').readlines()
    for line in fh:
        row = line.split(',')
    myConfig['username'] = row[0]
    myConfig['password'] = row[1]
    return myConfig


def sleepRandomLow():
    return random.randint(1, 3)


def getCity():
    whereIsPlayer = driver.find_elements(By.CLASS_NAME, "value")
    # print(whereIsPlayer)
    # for x in whereIsPlayer:
    # print(x.get_attribute("outerHTML"))
    fullWhere = whereIsPlayer[1].get_attribute("outerHTML")
    city = fullWhere[20:]
    city = city[:-7]
    return city


def login():
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


def krim():
    driver.find_element(By.LINK_TEXT, "Kriminalitet").click()
    checkAntiBot()
    isCounting = checkCountdown()
    if isCounting == False:
        # KRIMINALITET START
        time.sleep(1)
        driver.find_element(By.ID, "rowid_table_select_krimaction4").click()
        # KRIMINALITET END
    else:
        print("Timer is going")


def utpress():
    driver.find_element(By.LINK_TEXT, "Utpressing").click()
    checkAntiBot()
    isCounting = checkCountdown()
    if isCounting == False:
        # UTPRESSING START
        time.sleep(sleepRandomLow())
        driver.find_element(By.ID, "sel_1").click()
        time.sleep(sleepRandomLow())
        driver.find_element(By.NAME, "submitBlackmail").click()
        # UTPRESSING END
    else:
        print("Timer is going")


def fightclub():
    driver.find_element(By.LINK_TEXT, "Fightclub").click()
    checkAntiBot()
    isCounting = checkCountdown()
    if isCounting == False:
        # FIGHTCLUB START
        time.sleep(sleepRandomLow())
        driver.find_element(By.XPATH, "//td[text()='25 pushups']").click()
        # FIGHTCLUB END
    else:
        print("Timer is going")


def checkCountdown():
    isCountingDown = driver.find_elements(By.ID, "js_countdown")
    if len(isCountingDown) > 0:
        return True
    else:
        return False


def sendCar():
    currentCity = getCity()
    selectValue = random.randint(0, 5)
    time.sleep(sleepRandomLow())
    driver.find_element(By.XPATH, "//tr[@style='background-color: #ff4c4c;']").click()
    time.sleep(5)
    select = Select(driver.find_element(By.NAME, "targetcity"))
    time.sleep(sleepRandomLow())
    time.sleep(5)
    select.select_by_value(str(selectValue))
    time.sleep(5)
    targetCity = select.first_selected_option.text
    print("'" + currentCity + "'" + " " + "'" + targetCity + "'")
    if targetCity == currentCity:  # if trying to send to current city restart function
        print("RETRYING TO SEND CAR!")
        driver.refresh()
        sendCar()
    else:
        print("ACTUALLY SENDING CAR!")
        # actually send car
        time.sleep(sleepRandomLow())
        driver.find_element(By.NAME, "dotransport").click()
        time.sleep(sleepRandomLow())
        driver.find_element(By.NAME, "doTransport_confirm").click()


def biltyveri():
    # BILTYVERI START
    driver.find_element(By.LINK_TEXT, "Biltyveri/Garasje").click()
    checkAntiBot()
    isCounting = checkCountdown()
    if isCounting == False:
        time.sleep(sleepRandomLow() / 2)
        driver.find_element(By.ID, "rowid_table_select_gtaaction0").click()
        biltyveriSuccess = driver.find_elements(By.CLASS_NAME, "successBox")
        if len(biltyveriSuccess) > 0:
            sendCar()
    else:
        print("Timer is going")


def fengsel():
    driver.find_element(By.LINK_TEXT, "Fengsel").click()
    checkAntiBot()
    isCounting = checkCountdown()
    if isCounting == False:
        # FENGSEL START
        time.sleep(sleepRandomLow() / 2)
        if len(driver.find_elements(By.LINK_TEXT, "Bryt ut")) > 0:
            driver.find_element(By.LINK_TEXT, "Bryt ut").click()
        else:
            time.sleep(random.randint(30, 69))
        # FENGSEL END
        time.sleep(3)
        fengsel()
    else:
        print("Timer is going")





def timeDown():
    x = 0
    while x < 10:
        time.sleep(10)
        print("Sleep 10" + " " + x)
        x += 1


def doBotStuff():
    print("Start doBotStuff")
    timeDown()
    krim()
    fightclub()
    utpress()
    biltyveri()
    fengsel()
    doBotStuff()


def checkAntiBot():
    if len(driver.find_elements(By.XPATH, "//div[text()='Anti-bot']")) > 0:
        print("bot")
        time.sleep(sleepRandomLow()/2)
        solver = RecaptchaSolver(driver=driver)
        recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
        solver.click_recaptcha_v2(iframe=recaptcha_iframe)
    else:
        print("no bot")


login()
krim()
fightclub()
utpress()
biltyveri()
fengsel()
doBotStuff()
