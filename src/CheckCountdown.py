from selenium.webdriver.common.by import By


def checkCountdown(driver):
    isCountingDown = driver.find_elements(By.ID, "js_countdown")
    if len(isCountingDown) > 0:
        return True
    else:
        return False
