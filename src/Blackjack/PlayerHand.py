from selenium.webdriver.common.by import By

def playerHand(driver):
    try:
        Hand = driver.find_elements(By.CSS_SELECTOR, "div#playerHand1>div.cardsContainer>div.card")
        Card1 = Hand[0].get_attribute("data-card")
        Card2 = Hand[1].get_attribute("data-card")
        Card1 = Card1[:-1]
        Card2 = Card2[:-1]
        return int(Card1), int(Card2)
    except:
        print("div.playerHand1>div.cardsContainer>div.card")
        # Hit if cant find values
        return 10, 7
