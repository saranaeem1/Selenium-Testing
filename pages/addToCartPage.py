from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCart():
    def __init__(self, driver):
        self.driver = driver
        self.appleAddToCart = "mat-grid-tile:nth-child(1) > div > mat-card > div:nth-child(2) > button"
        self.pomaceAddToCart = "mat-grid-tile:nth-child(2) > div > mat-card > div:nth-child(2) > button"
        self.artworkAddToCart="mat-grid-tile:nth-child(4) > div > mat-card > div:nth-child(3) > button"
        self.permafrostAddToCart="mat-grid-tile:nth-child(9) > div > mat-card > div:nth-child(3) > button"
        self.message_cssSelector = ".mat-simple-snack-bar-content"
        self.basket_item_count = ".fa-layers-counter"

    def addAppleJuiceToCart(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.appleAddToCart))).click()

    def addPomaceToCart(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.pomaceAddToCart))).click()

    def addJuiceArtworkToCart(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.artworkAddToCart))).click()

    def addPermafrostToCart(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.permafrostAddToCart))).click()
        self.scroll_to_top()

    def message(self):
        msg = self.driver.find_element(By.CSS_SELECTOR, self.message_cssSelector).text
        return msg

    def basketCount(self):
        count = self.driver.find_element(By.CSS_SELECTOR, self.basket_item_count).text
        return count





