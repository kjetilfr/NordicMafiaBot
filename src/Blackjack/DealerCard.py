from selenium.webdriver.common.by import By

def dealerCard(driver):
    try:
        Card = driver.find_element(By.CSS_SELECTOR, "div.dealerHand>div.cardsContainer>div.card")
        Card = Card.get_attribute("data-card")
        Card = Card[:-1]
        return int(Card)
    except:
        print("div.dealerHand>div.cardsContainer>div.card")
        return 10
