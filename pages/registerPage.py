from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Register():
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox_id = "emailControl"
        self.password_textbox_id = "passwordControl" 
        self.repeat_password_textbox_id = "repeatPasswordControl"
        self.dropdown_name = "securityQuestion"
        self.security_answer = "//input[@id='securityAnswerControl']"
        self.submit_button_id = "registerButton"
        self.success_msg=".cdk-overlay-pane > snack-bar-container > div > div " + "simple-snack-bar >span"
        self.registered_email="/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-register/div/mat-card/div[1]"
        self.unmatched_password="/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-register/div/mat-card/div[2]/mat-form-field[3]/div/div[2]/div/mat-error"
    
    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def enter_repeat_password(self, repeat_password):
        self.driver.find_element(By.ID, self.repeat_password_textbox_id).send_keys(repeat_password)

    def click_dropdown(self, security_question):
        dropdown = self.driver.find_element(By.NAME, self.dropdown_name)
        dropdown.click()
        option_xpath = f"//mat-option/span[contains(text(), '{security_question}')]"
        option = self.driver.find_element(By.XPATH, option_xpath)
        option.click()

    def enter_security_answer(self, answer):
        self.driver.find_element(By.XPATH, self.security_answer).send_keys(answer)

    def click_register(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.submit_button_id))).click()

    def success_message(self):
        msg = self.driver.find_element(By.CSS_SELECTOR, self.success_msg).text
        return msg

    def reg_email(self):
        msg = self.driver.find_element(By.XPATH, self.registered_email).text
        return msg

    def password_notmatched(self):
        msg = self.driver.find_element(By.XPATH, self.unmatched_password).text
        return msg


