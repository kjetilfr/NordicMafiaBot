from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
from . import AntiBot
from . import CheckCountdown
from . import IsLoggedIn
from . import Bank
from . import GetMoney


def sleepRandomLow():
    return random.randint(1, 3)


def step1(driver):
    try:
        AntiBot.checkAntiBot(driver)
        movies = ["Zack and Miri Make a Porno", "Youth in Revolt", "You Will Meet a Tall Dark Stranger", "When in Rome", "What Happens in Vegas", "Water For Elephants", "WALL-E", "Waitress", "Waiting For Forever", "Valentine's Day", "Tyler Perry's Why Did I get Married", "Twilight: Breaking Dawn", "Twilight", "The Ugly Truth", "The Twilight Saga: New Moon", "The Time Traveler's Wife", "The Proposal", "The Invention of Lying", "The Heartbreak Kid", "The Duchess", "The Curious Case of Benjamin Button", "The Back-up Plan", "Tangled", "Something Borrowed", "She's Out of My League", "Sex and the City Two", "Sex and the City 2", "Sex and the City", "Remember Me", "Rachel Getting Married", "Penelope", "P.S. I Love You", "Over Her Dead Body", "Our Family Wedding", "One Day", "Not Easily Broken", "No Reservations", "Nick and Norah's Infinite Playlist", "New Year's Eve", "My Week with Marilyn", "Music and Lyrics", "Monte Carlo", "Miss Pettigrew Lives for a Day", "Midnight in Paris", "Marley and Me", "Mamma Mia!", "Mamma Mia!", "Made of Honor", "Love Happens", "Love & Other Drugs", "Life as We Know It", "License to Wed", "Letters to Juliet", "Leap Year", "Knocked Up", "Killers", "Just Wright", "Jane Eyre", "It's Complicated", "I Love You Phillip Morris", "High School Musical 3: Senior Year", "He's Just Not That Into You", "Good Luck Chuck", "Going the Distance", "Gnomeo and Juliet", "Gnomeo and Juliet", "Ghosts of Girlfriends Past", "Four Christmases", "Fireproof", "Enchanted", "Dear John", "Beginners", "Across the Universe", "A Serious Man", "A Dangerous Method", "27 Dresses", "(500) Days of Summer"]
        filmNameField = driver.find_element(By.NAME, "filmtitle")
        movieName = movies[random.randint(0, len(movies))]
        time.sleep(0.3)
        filmNameField.send_keys(movieName)
        movieGenreNmb = random.randint(0, 5)
        time.sleep(0.3)
        dropDownMenu = Select(driver.find_element(By.NAME, "filmgenre"))
        dropDownMenu.select_by_value(str(movieGenreNmb))
        time.sleep(0.3)
        print("Movie: Name: " + movieName + ". Genre: " + dropDownMenu.first_selected_option.text + ".")
        driver.find_element(By.NAME, "produceFilm").click()
        time.sleep(0.3)
        step2(driver)
    except:
        print("step1 failed or already completed")
        step2(driver)


def step2(driver):
    try:
        AntiBot.checkAntiBot(driver)
        driver.find_element(By.LINK_TEXT, "Filmproduksjon").click()
        time.sleep(0.3)
        driver.find_element(By.ID, "rowid_selected2").click()
        print(driver.find_element(By.ID, "rowid_selected2").get_attribute("innerHTML"))
        time.sleep(0.3)
        driver.find_element(By.NAME, "doselectactor").click()
        time.sleep(0.3)
        step3(driver)
    except:
        print("step2 failed or already completed")
        step3(driver)

def step3(driver):
    try:
        AntiBot.checkAntiBot(driver)
        driver.find_element(By.LINK_TEXT, "Filmproduksjon").click()
        time.sleep(0.3)
        driver.find_element(By.ID, "rowid_table_select_location2").click()
        print(driver.find_element(By.ID, "rowid_table_select_location2").get_attribute("innerHTML"))
        time.sleep(0.3)
        driver.find_element(By.ID, "rowid_table_select_equipment3").click()
        print(driver.find_element(By.ID, "rowid_table_select_equipment3").get_attribute("innerHTML"))
        time.sleep(0.3)
        driver.find_element(By.NAME, "doproceed").click()
        time.sleep(0.3)
        step4(driver)
    except:
        print("step3 failed or already completed")
        step4(driver)


def step4(driver):
    try:
        AntiBot.checkAntiBot(driver)
        driver.find_element(By.LINK_TEXT, "Filmproduksjon").click()
        time.sleep(0.3)
        driver.find_element(By.ID, "rowid_table_select_advertisement3").click()
        print(driver.find_element(By.ID, "rowid_table_select_advertisement3").get_attribute("innerHTML"))
        time.sleep(0.3)
        driver.find_element(By.ID, "rowid_table_select_release1").click()
        print(driver.find_element(By.ID, "rowid_table_select_release1").get_attribute("innerHTML"))

        time.sleep(0.3)
        driver.find_element(By.NAME, "doproceed").click()
        time.sleep(0.3)
        driver.find_element(By.LINK_TEXT, "Filmproduksjon").click()
        Bank.bankIdealAmount(driver)
    except:
        print("step4 failed or already completed")

def filmProd(driver):
    try:
        driver.find_element(By.LINK_TEXT, "Filmproduksjon").click()
        if IsLoggedIn.checkLogin(driver):
            if not CheckCountdown.checkCountdown(driver):
                Bank.withdrawAll(driver)
                if GetMoney.getMoney(driver) > 40000000:
                    time.sleep(0.5)
                    driver.find_element(By.LINK_TEXT, "Filmproduksjon").click()
                    step1(driver)
                else:
                    Bank.bankIdealAmount(driver)
                    print("Not enough money for film")
    except:
        print("driver.find_element(By.LINK_TEXT, Filmproduksjon).click() went wrong")
