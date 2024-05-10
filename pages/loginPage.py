from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Login():
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox_id = "email"
        self.password_textbox_id = "password" 
        self.login_button_id = "loginButton"
        self.logout_button_id="navbarLogoutButton"
        self.invalid_error="/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-login/div/mat-card/div[1]"
    
    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.login_button_id))).click()

    def success_login(self):
        account_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show/hide account menu']")))
        account_button.click()
        logout_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, self.logout_button_id)))
        a=logout_button.is_displayed()
        logout_button.click()
        return a

    def invalid_error_message(self):
        msg = self.driver.find_element(By.XPATH, self.invalid_error).text
        return msg

    


