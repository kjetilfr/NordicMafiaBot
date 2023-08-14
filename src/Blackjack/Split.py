from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from Settings import jsonRead
from src import IsLoggedIn
from . import DealerCard, PlayerHand, SoftTotal


def split(playerHand, dealerHand):
    print("SPLIT!")
    if playerHand[0] == 1:
        print("SPLIT!")
