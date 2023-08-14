from selenium.webdriver.common.by import By
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn
from . import GetCity
from . import GetMoney
from . import Bank

def sleepRandomLow():
    return random.randint(1, 3)


def buyEquipment(driver):
    try:
        # Check if have enough money
        if GetMoney.getMoney(driver) < 1500000:
            Bank.withdrawXAmount(driver, 1500000)
        driver.find_element(By.LINK_TEXT, "Organisert Krim").click()
        driver.find_element(By.ID, "rowid_table_select_selectEquipment6").click()
        time.sleep(sleepRandomLow())
        driver.find_element(By.NAME, "buyequipment").click()
    except:
        print("Tried to buy equipment")
        try:
            if GetMoney.getMoney(driver) < 1000000:
                Bank.withdrawXAmount(driver, 1000000)
            driver.find_element(By.LINK_TEXT, "Organisert Krim").click()
            driver.find_element(By.ID, "rowid_table_select_selectEquipment5").click()
            time.sleep(sleepRandomLow())
            driver.find_element(By.NAME, "buyequipment").click()
        except:
            print("Tried to buy 2nd equipment")
            try:
                if GetMoney.getMoney(driver) < 500000:
                    Bank.withdrawXAmount(driver, 500000)
                driver.find_element(By.LINK_TEXT, "Organisert Krim").click()
                driver.find_element(By.ID, "rowid_table_select_selectEquipment4").click()
                time.sleep(sleepRandomLow())
                driver.find_element(By.NAME, "buyequipment").click()
            except:
                print("Tried to buy 3rd equipment")



def joinLobby(driver):
    try:
        time.sleep(sleepRandomLow())
        driver.find_element(By.NAME, "joinPublicOC").click()
        time.sleep(sleepRandomLow())
        driver.find_element(By.LINK_TEXT, "Gå tilbake").click()
        time.sleep(sleepRandomLow())
        buyEquipment(driver)
    except:
        print("Kan ikke velge utstyr")


def makePublic(driver):
    time.sleep(0.2)
    try:
        if not driver.find_element(By.ID, "ocMode_public").get_attribute("style") == "background-color: green;":
            time.sleep(0.2)
            driver.find_element(By.ID, "ocMode_public").click()
            time.sleep(sleepRandomLow() / 2)
            driver.find_element(By.NAME, "saveChanges").click()
            time.sleep(sleepRandomLow() / 2)
            driver.find_element(By.LINK_TEXT, "Gå tilbake").click()
    except:
        print("Already public or failed getting oc")

def createLobby(driver):
    try:
        if GetMoney.getMoney(driver) < 400000:
            Bank.withdrawXAmount(driver, 400000)
        driver.find_element(By.NAME, "createOC").click()
        time.sleep(sleepRandomLow() / 2)
        makePublic(driver)
    except:
        print("Kan ikke lage lobby")


def isInOC(driver):
    try:
        elems = driver.find_elements(By.NAME, "createOC")
        if len(elems) > 0:
            return True
        else:
            return False
    except:
        print("Cant find element createOC")


def utforOK(driver):
    # CHECK TIMER
    if isInOC(driver):
        # IS NOT IN LOBBY
        currentCity = GetCity.getCity(driver)
        # TRY CATCH/EXCEPT IN CASE OF ERROR
        try:
            # Get all active (full) elements
            lobbies = driver.find_elements(By.CSS_SELECTOR, "tr.highlightrow>td:nth-child(2)")
            # Extract city names and make a list of the cities
            listOfLobbies = []
            for l in lobbies:
                listOfLobbies.append(l.get_attribute("innerHTML"))
            # If there is a lobby in your city join it, if not create a lobby
            if currentCity in listOfLobbies:
                # Join lobby
                positionOfCurrentCity = listOfLobbies.index(currentCity)
                lobbies[positionOfCurrentCity].click()
                joinLobby(driver)
            else:
                # Create own lobby
                createLobby(driver)
        except:
            print("Cant create/join lobby")
    else:
        # IS IN LOBBY
        if len(driver.find_elements(By.NAME, "canceloc")) > 0:
            # SELF HOSTED LOBBY
            playersReady = driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td>span.notready")
            # check how many players are not ready
            playersNotReady = sum(i.get_attribute("innerHTML") == "Ikke klar" for i in playersReady)
            if playersNotReady == 1:
                # Start lobby (Only host not ready)
                print("Choose gear and start lobby")
        else:
            # JOINED A PUBLIC LOBBY
            if len(driver.find_elements(By.ID, "oc_buyequipment_button")) > 0:
                buyEquipment(driver)
    makePublic(driver)
    print("Er i public lobby")



def orgKrim(driver):
    try:
        driver.find_element(By.LINK_TEXT, "Organisert Krim").click()
        #Checktimer
        element = driver.find_element(By.CSS_SELECTOR, "div.blockInstance.blockInstanceWideX2>div.bHeader")
        if "Du må vente" in element.get_attribute("innerHTML"):
            print("OC timer going")
        else:
            # Make lobby public if not public
            isLobbyPublicCount = driver.find_elements(By.ID, "ocMode_public")
            isLobbyPublic = driver.find_element(By.ID, "ocMode_public")
            if len(isLobbyPublicCount) > 0:
                if not isLobbyPublic.get_attribute("style") == "background-color: green;":
                    makePublic(driver)
                else:
                    print("lobby is public")
    except:
        print("driver.find_element(By.LINK_TEXT, Organisert Krim).click() went wrong")
        if IsLoggedIn.checkLogin(driver):
            utforOK(driver)
        else:
            try:
                driver.find_element(By.LINK_TEXT, "Organisert Krim").click()
            except:
                print("driver.find_element(By.LINK_TEXT, Organisert Krim).click() went wrong 2")
            utforOK(driver)
