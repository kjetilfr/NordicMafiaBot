from selenium import webdriver
import time
import random
from Settings import jsonRead
from src import *
from fake_useragent import UserAgent
import datetime

jsonData = jsonRead.loadProfile()

ua = UserAgent()
user_agent = ua.random
options = webdriver.FirefoxOptions()
if jsonData[0]["Headless"] == 1:
    options.add_argument("--headless")
    print("HEADLESS MODE (MIGHT NOT WORK OR MIGHT RESULT IN BAN! USE AT OWN RISK")
    print("HEADLESS MODE MIGHT BREAK ANTIBOT FEATURES!")
if jsonData[0]["Proxy"] == 1:
    proxy_server_url = jsonData[0]["ProxyIP"] + ":" + jsonData[0]["ProxyPort"]
    options.add_argument(f'--proxy-server={proxy_server_url}')

options.add_argument("--window-size=1920,1080")

chrome_driver_binary = "C:/chromedriver"
options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")
options.add_argument(f'--user-agent={user_agent}')
options.set_preference('intl.accept_languages', 'en-GB')

driver = webdriver.Firefox(options=options)
driver.get("https://nordicmafia.org")


def timeDown():
    sleepTime = random.randint(230, 280)
    print("Sleep " + str(sleepTime))
    time.sleep(sleepTime)


def doBotStuff():
    while True:
        print("Start doBotStuff")
        timeDown()
        Bunker.gaaIBunkerCheck(driver)

        Bank.bankIdealAmount(driver)
        if jsonData[2]["Hasjplantasje"] == 1:
            Hasjplantasje.hasj(driver)
        else:
            if GetMoney.getMoney(driver) > 3000000:
                Bank.bankIdealAmount(driver)
        Kriminalitet.krim(driver, jsonData[2]["Kriminalitet"])
        Utpressing.utpress(driver, jsonData[2]["Utpressing"], jsonData[2]["UtpressingPerson"])
        FightClub.fightclub(driver, jsonData[2]["Fightclub"])
        if jsonData[2]["Organisert Kriminalitet"] == 1:
            OrganisertKriminalitet.orgKrim(driver)
        if jsonData[2]["Filmproduksjon"] == 1:
            Filmproduksjon.filmProd(driver)
        Biltyveri.biltyveri(driver, jsonData[2]["Biltyveri"])
        if jsonData[2]["Fengsel"] == 1:
            Fengsel.fengsel(driver)
        if jsonData[3]["LongTimeout"] == 1:
            LongBreak.isBetweenTime(driver)


def doBotStuffMenyTimer():
    while True:
        print("Checking timers")
        time.sleep(20)
        AntiBot.checkAntiBot(driver)
        IsLoggedIn.checkLogin(driver)
        if GetTimer.getTimer(driver, "Fengsel") == 0:
            #if datetime.time(18, 57, 00) <= GetTime.checkClock(driver) <= datetime.time(18, 58, 00):
            #    Sok.start_sok_personer(driver)
            #    Sok.start_sok_varger(driver)
            Bunker.gaaIBunkerCheck(driver)
            if GetMoney.getMoney(driver) > 1200000:
                Bank.bankIdealAmount(driver)
            if jsonData[2]["Hasjplantasje"] == 1:
                Hasjplantasje.hasj(driver)
            else:
                if GetMoney.getMoney(driver) > 1200000:
                    Bank.depositXAmount(driver, 1000000)
        if GetTimer.getTimer(driver, "Kriminalitet") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
            Kriminalitet.krim(driver, jsonData[2]["Kriminalitet"])
        if GetTimer.getTimer(driver, "Utpressing") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
            Utpressing.utpress(driver, jsonData[2]["Utpressing"], jsonData[2]["UtpressingPerson"])
        if GetTimer.getTimer(driver, "Fightclub") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
            FightClub.fightclub(driver, jsonData[2]["Fightclub"])
        if GetTimer.getTimer(driver, "Livvakter") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
            if jsonData[2]["Livvakt"] == 1:
                Livvaktutleie.livvaktutleie(driver)
        if jsonData[2]["Organisert Kriminalitet"] == 1:
            if GetTimer.getTimer(driver, "Organisert Kriminalitet") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
                OrganisertKriminalitet.orgKrim(driver)
        if jsonData[2]["Filmproduksjon"] == 1:
            if GetTimer.getTimer(driver, "Filmproduksjon") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
                Filmproduksjon.filmProd(driver)
        if jsonData[2]["CDG"] == 1:
            if GetTimer.getTimer(driver, "Club dè gangster") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
                CDG.cdg(driver, jsonData[2]["CDGPerson"], jsonData[2]["Gangstere"])
        if GetTimer.getTimer(driver, "Biltyveri") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0  and not datetime.time(18, 50, 00) <= GetTime.checkClock(driver) <= datetime.time(19, 10, 00):
            Biltyveri.biltyveri(driver, jsonData[2]["Biltyveri"])
        if GetTimer.getTimer(driver, "Fengsel") == 0:
            if GetTimer.getTimer(driver, "Kriminalitet") == 0:
                pass
            else:
                if jsonData[2]["Fengsel"] == 1 and not datetime.time(18, 50, 00) <= GetTime.checkClock(driver) <= datetime.time(19, 10, 00):
                    Fengsel.fengsel(driver)
        if jsonData[3]["LongTimeout"] == 1:
            LongBreak.isBetweenTime(driver)


def startBot():
    Login.login(driver)
    if jsonData[2]["Livvakt"] == 1:
        Livvaktutleie.livvaktutleie(driver)
    Bank.bankIdealAmount(driver)
    if jsonData[2]["Hasjplantasje"] == 1:
        Hasjplantasje.hasj(driver)
    else:
        if GetMoney.getMoney(driver) > 3000000:
            Bank.depositXAmount(driver, 1000000)
    Kriminalitet.krim(driver, jsonData[2]["Kriminalitet"])
    Utpressing.utpress(driver, jsonData[2]["Utpressing"], jsonData[2]["UtpressingPerson"])
    FightClub.fightclub(driver, jsonData[2]["Fightclub"])
    if jsonData[2]["Organisert Kriminalitet"] == 1:
        OrganisertKriminalitet.orgKrim(driver)
    if jsonData[2]["Filmproduksjon"] == 1:
        Filmproduksjon.filmProd(driver)
    Biltyveri.biltyveri(driver, jsonData[2]["Biltyveri"])
    Bunker.gaaIBunkerCheck(driver)
    if jsonData[2]["Fengsel"] == 1:
        Fengsel.fengsel(driver)
    doBotStuff()


def startBotMenyTimer():
    Login.login(driver)
    IsInBunker.bunker(driver)
    if GetTimer.getTimer(driver, "Fengsel") == 0:
        IsInBunker.bunker(driver)
        Bunker.gaaIBunkerCheck(driver)
        Bank.bankIdealAmount(driver)
        if jsonData[2]["Hasjplantasje"] == 1:
            Hasjplantasje.hasj(driver)
        else:
            if GetMoney.getMoney(driver) > 3000000:
                Bank.depositXAmount(driver, 3000000)
    if GetTimer.getTimer(driver, "Livvakter") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
        if jsonData[2]["Livvakt"] == 1:
            Livvaktutleie.livvaktutleie(driver)
    if GetTimer.getTimer(driver, "Kriminalitet") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
        Kriminalitet.krim(driver, jsonData[2]["Kriminalitet"])
    if GetTimer.getTimer(driver, "Utpressing") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
        Utpressing.utpress(driver, jsonData[2]["Utpressing"], jsonData[2]["UtpressingPerson"])
    if GetTimer.getTimer(driver, "Fightclub") == 0:
        FightClub.fightclub(driver, jsonData[2]["Fightclub"])
    if jsonData[2]["Organisert Kriminalitet"] == 1:
        if GetTimer.getTimer(driver, "Organisert Kriminalitet") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
            OrganisertKriminalitet.orgKrim(driver)
    if jsonData[2]["Filmproduksjon"] == 1:
        if GetTimer.getTimer(driver, "Filmproduksjon") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
            Filmproduksjon.filmProd(driver)
    if jsonData[2]["CDG"] == 1:
        if GetTimer.getTimer(driver, "Club dè gangster") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
            CDG.cdg(driver, jsonData[2]["CDGPerson"], jsonData[2]["Gangstere"])
    if GetTimer.getTimer(driver, "Biltyveri") == 0 and GetTimer.getTimer(driver, "Fengsel") == 0:
        Biltyveri.biltyveri(driver, jsonData[2]["Biltyveri"])
    if GetTimer.getTimer(driver, "Fengsel") == 0:
        if jsonData[2]["Fengsel"] == 1:
            Fengsel.fengsel(driver)
    doBotStuffMenyTimer()


if jsonData[0]["Menytimer"] == 1:
    print("Menytimer")
    startBotMenyTimer()
else:
    startBot()

time.sleep(20000)
