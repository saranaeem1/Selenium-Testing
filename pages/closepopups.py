from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClosePopups:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_popup_xpath = "//button[@aria-label='Close Welcome Banner']"
        self.cookie_popup_xpath = "//a[@aria-label='dismiss cookie message']"
    
    def click_welcome_button(self):
        welcome_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.welcome_popup_xpath)))
        welcome_button.click()

    def click_cookie_button(self):
        cookie_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cookie_popup_xpath)))
        cookie_button.click()
