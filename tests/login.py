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
from loginPage import  Login

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://demo.owasp-juice.shop/")
        time.sleep(2)

    def navigateToLogin(self):
        # Find account button to click it
        account_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show/hide account menu']")))
        account_button.click()
        # Click on login
        login_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "navbarLoginButton")))
        login_button.click()

    #Test case for valid login
    def test_01valid_login(self):
        driver = self.driver
        popup_close = ClosePopups(driver)
        popup_close.click_welcome_button()
        popup_close.click_cookie_button()
        time.sleep(2)
        self.navigateToLogin()
        signin=Login(driver)
        signin.enter_email("sara40@gmail.com")
        signin.enter_password("Sara123$")
        time.sleep(1)
        signin.click_login()
        time.sleep(2)
        self.assertTrue(signin.success_login())
        time.sleep(5)

    #Test case for invalid email
    def test_02invalid_email(self):
        driver = self.driver
        self.navigateToLogin()
        signin=Login(driver)
        signin.enter_email("sara99@gmail.com")
        signin.enter_password("Sara123$")
        time.sleep(1)
        signin.click_login()
        time.sleep(5)
        errorMsg=signin.invalid_error_message()
        expected_error_message = "Invalid email or password."
        self.assertEqual(errorMsg, expected_error_message)

    #Test case for invalid password
    def test_03invalid_password(self):
        driver = self.driver
        self.navigateToLogin()
        signin=Login(driver)
        signin.enter_email("sara40@gmail.com")
        signin.enter_password("Sara12")
        time.sleep(1)
        signin.click_login()
        time.sleep(5)
        errorMsg=signin.invalid_error_message()
        expected_error_message = "Invalid email or password."
        self.assertEqual(errorMsg, expected_error_message)
    
    #Test case for invalid email and invalid password
    def test_04invalid_email_password(self):
        driver = self.driver
        self.navigateToLogin()
        signin=Login(driver)
        signin.enter_email("sara99@gmail.com")
        signin.enter_password("Sara12")
        time.sleep(1)
        signin.click_login()
        time.sleep(5)
        errorMsg=signin.invalid_error_message()
        expected_error_message = "Invalid email or password."
        self.assertEqual(errorMsg, expected_error_message)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))

    