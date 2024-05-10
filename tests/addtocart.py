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
from addToCartPage import  AddToCart

class TestAddToCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://demo.owasp-juice.shop/")
        time.sleep(2)

    def login(self):
        popup_close = ClosePopups(self.driver)
        popup_close.click_welcome_button()
        popup_close.click_cookie_button()
        account_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show/hide account menu']")))
        account_button.click()
        login_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "navbarLoginButton")))
        login_button.click()
        signin = Login(self.driver)
        signin.enter_email("sara40@gmail.com")
        signin.enter_password("Sara123$")
        time.sleep(1)
        signin.click_login()

    #Test case for valid add to cart
    def test_01valid_addToCart(self):
        driver = self.driver
        self.login()
        add = AddToCart(driver)
        add.addAppleJuiceToCart()
        time.sleep(5)
        successMsg = add.message()
        expectedsuccessMsg="Placed Apple Juice (1000ml) into basket."
        self.assertEqual(successMsg, expectedsuccessMsg)
        add.addPomaceToCart()
        time.sleep(5)
        successMsg2 = add.message()
        expectedsuccessMsg2="Placed Apple Pomace into basket."
        self.assertEqual(successMsg2, expectedsuccessMsg2)
        count=add.basketCount()
        expectedCount="2"
        self.assertEqual(count, expectedCount)
        time.sleep(6)

    #Test case for adding item more than quantity available
    def test_02add_more_than_quantity(self):
        driver = self.driver
        add = AddToCart(driver)
        add.addPermafrostToCart()
        time.sleep(5)
        successMsg = add.message()
        expectedsuccessMsg='Placed Juice Shop "Permafrost" 2020 Edition into basket.'
        self.assertEqual(successMsg, expectedsuccessMsg)
        add.addPermafrostToCart()
        time.sleep(5)
        errorMsg = add.message()
        expectedErrorMsg="You can order only up to 1 items of this product."
        self.assertEqual(errorMsg, expectedErrorMsg)
        count=add.basketCount()
        expectedCount="3"
        self.assertEqual(count, expectedCount)

    #Test case for adding soldout items
    def test_03add_soldout_items(self):
        driver = self.driver
        add = AddToCart(driver)
        add.addJuiceArtworkToCart()
        time.sleep(5)
        errorMsg = add.message()
        expectedErrorMsg="We are out of stock! Sorry for the inconvenience."
        self.assertEqual(errorMsg, expectedErrorMsg)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))


    



