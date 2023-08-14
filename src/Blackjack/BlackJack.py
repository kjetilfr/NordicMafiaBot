from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from Settings import jsonRead
from src import IsLoggedIn
from . import DealerCard, PlayerHand, SoftTotal, Split


def playBlackJack(driver):
    chip = driver.find_element(By.ID, "chipsContainer").get_attribute("style")
    # try to locate betting chips
    #if betting chips element exists, click it and continue blackjack play
    if chip == "display: block;":
        print(chip)
        #Bet 2 coins
        #WHEN DEALING DO THIS FIRST IF HAS DEALT DO SOMETHING ELSE
        # WHEN DEALING DO THIS FIRST IF HAS DEALT DO SOMETHING ELSE
        # WHEN DEALING DO THIS FIRST IF HAS DEALT DO SOMETHING ELSE
        # WHEN DEALING DO THIS FIRST IF HAS DEALT DO SOMETHING ELSE
        driver.find_element(By.XPATH, "//*[@class='chip chip_1']").click()
        time.sleep(2)
        try:
            driver.find_element(By.ID, "btnDeal").click()
            time.sleep(2)
            dealerCard = DealerCard.dealerCard(driver)
            print(dealerCard)
            playerCard = PlayerHand.playerHand(driver)
            print(playerCard)
            if playerCard[0] == playerCard[1]:
                Split.split(playerCard, dealerCard)
            if playerCard[0] == 1 or playerCard[1] == 1:
                SoftTotal.softTotal(playerCard, dealerCard)
            print("Sleep")
            time.sleep(500)
        except:
            time.sleep(500)
            print("btnDeal not found")
        time.sleep(2)
    elif chip == "display: none;":
        # if display none Rebet or play hand
        try:
            driver.find_element(By.ID, "btnRebet").click()
        except:
            print("Play normal hand of blackjack")
            time.sleep(1000)
    else:
        # if none are found try
        print("Hand is going play normal blackjack")
        time.sleep(400)


def blackjack(driver):
    IsLoggedIn.checkLogin(driver)
    # TRY CATCH/EXCEPT IN CASE OF ERROR
    try:
        driver.find_element(By.LINK_TEXT, "Blackjack").click()
    except:
        print("driver.find_element(By.LINK_TEXT, Blackjack).click() went wrong")
    if IsLoggedIn.checkLogin(driver):
        playBlackJack(driver)
    else:
        try:
            driver.find_element(By.LINK_TEXT, "Blackjack").click()
        except:
            print("driver.find_element(By.LINK_TEXT, Blackjack).click() went wrong 2")
        playBlackJack(driver)
