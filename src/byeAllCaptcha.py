import shutil
import urllib.request
import requests
import urllib3
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from random import uniform, randint
import urllib
from . import analyse_img
import json
from byerecaptcha import solveRecaptcha


def set_captcha_frames(driver):
    print("set_captcha_frames")
    global check_box_iframe, image_iframe
    time.sleep(1)
    recaptchaFrames = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "iframe")))

    for frames in recaptchaFrames:
        if frames.get_attribute("title") == "reCAPTCHA":
            check_box_iframe = frames
        elif frames.get_attribute("title") == "recaptcha challenge expires in two minutes":
            image_iframe = frames


def download_image(driver):
    print("dl img")
    driver.switch_to.frame(image_iframe)
    elem = driver.find_element(By.TAG_NAME, "img")
    url = elem.get_attribute("src")
    urllib.request.urlretrieve(url, "payload.jpg")
    driver.switch_to.parent_frame()


def read_json(driver):
    print("read_json")
    driver.switch_to.frame(image_iframe)
    print("swap")
    lookfor = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div>div>strong")))
    lookfor = lookfor.get_attribute("innerHTML")
    f = open('classes.json')
    data = json.load(f)
    print("reading")
    number = data[lookfor]
    f.close()
    driver.switch_to.parent_frame()
    return int(number)


def click_verify(driver):
    print("click_verify")
    driver.switch_to.frame(image_iframe)
    verify_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "recaptcha-verify-button")))
    verify_button.click()
    driver.switch_to.parent_frame()


def check_if_done(driver):
    print("checkifdone")
    # driver.switch_to.frame(image_iframe)
    # time.sleep(1)
    # canfindbluetext = driver.find_elements(By.CSS_SELECTOR, '.rc-imageselect-desc-no-canonical>span')
    # driver.switch_to.parent_frame()
    # if len(canfindbluetext) != 0:
    #     return False
    # else:
    #     return True
    time.sleep(1)
    divs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'div')))
    for div in divs:
        #if div.get_attribute("outerHTML") == '<div style="border-color: transparent rgb(255, 255, 255) transparent transparent; border-style: solid; border-width: 10px; border-image: none 100% / 1 / 0 stretch; width: 0px; height: 0px; position: absolute; pointer-events: none; margin-top: -10px; z-index: 2000000000; top: 290px; right: 100%;" class="g-recaptcha-bubble-arrow"></div>':
        if div.get_attribute("outerHTML") == '<div style="background-color: rgb(255, 255, 255); border: 1px solid rgb(204, 204, 204); box-shadow: rgba(0, 0, 0, 0.2) 2px 2px 3px; position: absolute; transition: visibility 0s linear 0.3s, opacity 0.3s linear 0s; opacity: 0; visibility: hidden; z-index: 2000000000; left: 84px; top: -10000px;"><div style="width: 100%; height: 100%; position: fixed; top: 0px; left: 0px; z-index: 2000000000; background-color: rgb(255, 255, 255); opacity: 0.05;"></div><div class="g-recaptcha-bubble-arrow" style="border-width: 11px; border-style: solid; border-color: transparent rgb(204, 204, 204) transparent transparent; border-image: initial; width: 0px; height: 0px; position: absolute; pointer-events: none; margin-top: -11px; z-index: 2000000000; top: 290px; right: 100%;"></div>':
            print("YES")
            return True
        else:
            print("NO")
    return False


def solve_type(driver):
    print("solve_type")
    driver.switch_to.frame(image_iframe)
    typeOfSolve = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.rc-imageselect-desc-no-canonical>span')))
    if typeOfSolve.get_attribute("innerHTML") == "If there are none, click skip":
        print("Solve 4 x 4")
        driver.switch_to.parent_frame()
        return "Solve 4 x 4"
    else:
        print("Solve 3 x 3")
        driver.switch_to.parent_frame()
        return "Solve 3 x 3"


def click_refresh(driver):
    print("refresh")
    driver.switch_to.frame(image_iframe)
    refresh_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "recaptcha-reload-button")))
    refresh_button.click()
    driver.switch_to.parent_frame()


def click_checkbox(driver):
    print("checkbox")
    driver.switch_to.frame(check_box_iframe)
    check_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "recaptcha-anchor")))
    time.sleep(0.4)
    check_box.click()
    driver.switch_to.parent_frame()


def click_items(driver):
    print("clickitems")
    json_data = read_json(driver)
    if read_json(driver) != 0:
        driver.switch_to.frame(image_iframe)
        click_array = analyse_img.get_click_array(json_data)
        tableGrid = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "rc-imageselect-tile")))
        for index, item in enumerate(tableGrid):
            if click_array[index]:
                item.click()
        driver.switch_to.parent_frame()
    else:
        click_refresh(driver)
        click_items(driver)


def click_items_3x3(driver):
    print("clickitems3x3")
    json_data = read_json(driver)
    if read_json(driver) != 0:
        driver.switch_to.frame(image_iframe)
        click_array = analyse_img.get_click_array_3x3(json_data)
        tableGrid = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "rc-imageselect-tile")))
        for index, item in enumerate(tableGrid):
            if click_array[index]:
                item.click()
        driver.switch_to.parent_frame()
    else:
        click_refresh(driver)
        click_items(driver)


def solve_grid(driver):
    print("solvegrid")
    if check_if_done(driver) == False:
        solve_typ = solve_type(driver)
        if solve_typ == "Solve 4 x 4":
            download_image(driver)
            click_items(driver)
            driver.switch_to.parent_frame()
            click_verify(driver)
            time.sleep(1)
            solve_grid(driver)
        else:
            print("StartRecaptcha")
            solveRecaptcha(driver)
            print("DoneRecaptcha")
            # download_image(driver)
            # click_items_3x3(driver)
            # driver.switch_to.parent_frame()
            # click_verify(driver)
            # time.sleep(1)
            # solve_grid(driver)
    else:
        return True


def solve_recaptcha(browser):
    print("start")
    # Set global iFrames
    set_captcha_frames(browser)

    click_checkbox(browser)

    solve_grid(browser)

    time.sleep(4)
