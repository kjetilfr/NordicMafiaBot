from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from Settings import jsonRead
from src import IsLoggedIn
from . import DealerCard, PlayerHand, SoftTotal


def softTotal(playerHand, dealerHand):
    if playerHand[0] + playerHand[1]:
        print(str(playerHand) + " " + str(dealerHand))
