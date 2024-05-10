from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import sys
import os
import HtmlTestRunner
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))
from closepopups import ClosePopups 
from registerPage import  Register

class RegisterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://demo.owasp-juice.shop/")
        time.sleep(2)

    def navigateToRegisterPage(self):
        # Find account button to click it
        account_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show/hide account menu']")))
        account_button.click()
        # Click on login
        login_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "navbarLoginButton")))
        login_button.click()
        # Click on not yet a customer link
        login_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "newCustomerLink")))
        login_button.click()

    # Test case for valid registration
    def test_01valid_registration(self):
        driver = self.driver
        popup_close = ClosePopups(driver)
        popup_close.click_welcome_button()
        popup_close.click_cookie_button()
        self.navigateToRegisterPage()
        reg = Register(self.driver)
        reg.enter_email("sara42@gmail.com")
        reg.enter_password("Sara123$")
        reg.enter_repeat_password("Sara123$")
        reg.click_dropdown(" Your eldest siblings middle name? ")
        time.sleep(3)
        reg.enter_security_answer("naeem")
        reg.click_register()
        time.sleep(5)
        successMsg = reg.success_message()
        expected_success_message = "Registration completed successfully. You can now log in."
        self.assertEqual(successMsg, expected_success_message)

    # Test case for email already registered
    def test_02invalid_email(self):
        self.navigateToRegisterPage()
        reg = Register(self.driver)
        reg.enter_email("sara40@gmail.com")
        reg.enter_password("Sara123$")
        reg.enter_repeat_password("Sara123$")
        reg.click_dropdown(" Your eldest siblings middle name? ")
        time.sleep(3)
        reg.enter_security_answer("naeem")
        reg.click_register()
        time.sleep(5)
        errorMsg = reg.reg_email()
        expected_error_message = "Email must be unique"
        self.assertEqual(errorMsg, expected_error_message)

    # Test case for password don't match
    def test_03invalid_password(self):
        self.navigateToRegisterPage()
        reg = Register(self.driver)
        reg.enter_email("sara23@gmail.com")
        reg.enter_password("Sara12$")
        reg.enter_repeat_password("Sara123$")
        reg.click_dropdown("Your eldest siblings middle name?")
        time.sleep(3)
        reg.enter_security_answer("naeem")
        time.sleep(5)
        errorMsg = reg.password_notmatched()
        expected_error_message = "Passwords do not match"
        self.assertEqual(errorMsg, expected_error_message)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
