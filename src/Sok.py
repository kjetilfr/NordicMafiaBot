from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from . import IsLoggedIn
from . import Bank
import json
import time

mod_list = ["Megan Fox", "Silver Fox", "Andrew", "Christian", "Erlend", "Kristian", "Nyan Cat", "System"]


def new_players(driver):
    IsLoggedIn.checkLogin(driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Spillstatistikk"))).click()

    new_player_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.blockInstance.blockInstanceWide")))

    username_elements = new_player_table.find_elements(By.CSS_SELECTOR, "table>tbody>tr>td>a")

    new_users = []
    for username in username_elements:
        new_users.append(username.get_attribute("innerHTML"))
    return new_users


def fengsel_players(driver):
    IsLoggedIn.checkLogin(driver)
    if driver.current_url != "https://nordicmafia.org/index.php?p=jail":
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Fengsel"))).click()
    fengsel_users = []
    everyoneInJail = driver.find_elements(By.CSS_SELECTOR,
                                          "table.def_table.def_table_left.coloringTable>tbody>tr")
    for p in everyoneInJail[1:]:
        test = p.find_element(By.CSS_SELECTOR, "a")
        if len(p.find_elements(By.CSS_SELECTOR, "a>span")) > 0:
            fengsel_users.append(p.find_element(By.CSS_SELECTOR, "span").get_attribute("innerHTML"))
        else:
            test = test.get_attribute("innerHTML")[27:]
            fengsel_users.append(test)

    return fengsel_users


def dead_players(driver):
    IsLoggedIn.checkLogin(driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Dagens mord"))).click()

    dead_player_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "tdsmurders_listtable")))

    username_elements = dead_player_table.find_elements(By.CSS_SELECTOR, "a")

    dead_users = []
    for username in username_elements:
        dead_users.append(username.get_attribute("innerHTML"))
    return dead_users


def write_to_file(player_array):
    print("writing to file")
    with open("./Settings/users.json", "r+") as f:
        data = json.load(f)
        users = data["users"]
        vargs = data["npcs"]
        for player in player_array:
            if not player in users:
                if not player in vargs:
                    if not player in mod_list:
                        users.append(player)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        f.close()


def write_to_file_dead_players(player_array):
    print("Removing dead players")
    with open("./Settings/users.json", "r+") as f:
        data = json.load(f)
        users = data["users"]
        for player in player_array:
            if player in users:
                print(player)
                users.remove(player)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        f.close()


def read_file():
    f = open('./Settings/users.json')
    data = json.load(f)
    f.close()
    return data


def count_users():
    f = open('./Settings/users.json')
    data = json.load(f)
    f.close()
    return int(len(data["users"]))


def start_aktivt_sok_personer(driver):
    Bank.withdrawAll(driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Aktiv detektiv"))).click()
    data = read_file()
    personer = data["users"]
    for person in personer:
        victim_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "detectivename")))
        victim_field.send_keys(person)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "dosearch"))).click()
        time.sleep(0.2)
    time.sleep(1)
    Bank.depositAll(driver)


def start_aktivt_sok_varger(driver):
    Bank.withdrawAll(driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Aktiv detektiv"))).click()
    data = read_file()
    varger = data["npcs"]
    for person in varger:
        victim_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "detectivename")))
        victim_field.send_keys(person)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "dosearch"))).click()
        time.sleep(0.2)
    time.sleep(1)
    Bank.depositAll(driver)

def start_vanlig_sok_personer(driver):
    Bank.withdrawAll(driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Drep"))).click()
    data = read_file()
    personer = data["users"]
    i = 0
    while i < len(personer) / 3:
        driver.get("https://nordicmafia.org/index.php?p=kill")
        victim_field = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "detectivename")))
        driver.find_element(By.NAME, "citychoice").click()
        victim_field.send_keys(personer[0])
        victim_field.send_keys(", ")
        victim_field.send_keys(personer[1])
        victim_field.send_keys(", ")
        victim_field.send_keys(personer[2])
        personer.pop(0)
        personer.pop(0)
        personer.pop(0)
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "dosearch"))).click()
        i += 1
        time.sleep(0.02)
    time.sleep(1)
    Bank.depositAll(driver)


def start_vanlig_sok_varger(driver):
    Bank.withdrawAll(driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Drep"))).click()
    data = read_file()
    varger = data["npcs"]
    i = 0
    while i < len(varger):
        driver.get("https://nordicmafia.org/index.php?p=kill")
        victim_field = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "detectivename")))
        driver.find_element(By.NAME, "citychoice").click()
        victim_field.send_keys(varger[0])
        varger.pop(0)
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "dosearch"))).click()
        i += 1
        time.sleep(0.02)
    time.sleep(1)
    Bank.depositAll(driver)


def start_sok_array(person_array, driver):
    Bank.withdrawAll(driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Aktiv detektiv"))).click()
    for person in person_array:
        victim_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "detectivename")))
        victim_field.send_keys(person)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "dosearch"))).click()
        time.sleep(0.2)
    Bank.depositAll(driver)


def sekund_sok(person, antall_sekunder, driver):
    Bank.withdrawAll(driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Aktiv detektiv"))).click()
    victim_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "detectivename")))
    victim_field.send_keys(person)
    second_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "search_secounds")))
    second_field.send_keys(Keys.BACKSPACE)
    second_field.send_keys(antall_sekunder)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "dosearch"))).click()
    time.sleep(0.2)


def aktive_spillere(driver):
    IsLoggedIn.checkLogin(driver)
    header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "helpHeader")))

    WebDriverWait(header, 10).until(EC.presence_of_element_located((By.TAG_NAME, "a"))).click()

    content_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.contentBox")))

    username_elements = content_box.find_elements(By.CSS_SELECTOR, "a")

    users = []
    for username in username_elements:
        users.append(username.get_attribute("innerHTML"))
    return users


def sjekk_dod(driver):
    #send kule på 1kr
    #er dod = remove frå liste
    # går gjennom = canceller kule
    print("removed")
    #finito

