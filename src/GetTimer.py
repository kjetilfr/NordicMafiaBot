from selenium.webdriver.common.by import By
import time


def getTimer(driver, timerType):
    time.sleep(0.5)
    try:
        allTimers = driver.find_elements(By.CSS_SELECTOR, "div.actionMenuContainer>div")
        for t in allTimers:
            timer = t.get_attribute("data-tooltip-content")
            if timerType in timer:
                if timerType == "Fengsel" and len(t.find_elements(By.CSS_SELECTOR, "div>span")) < 1:
                    return 0
                timerElement = t.find_element(By.CSS_SELECTOR, "div>span")
                timerText = timerElement.get_attribute("innerHTML")
                return int(timerText)
            if timerType == "Fengsel" and timerType not in timer:
                return 0
    except:
        print("Failed getting timer, returning 0")
        return 0




