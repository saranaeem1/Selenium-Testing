from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import sys
import os
import HtmlTestRunner
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))
from closepopups import ClosePopups 

class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://demo.owasp-juice.shop/")
        time.sleep(2)

    #Test case for searching element that is present
    def test_01SuccessfulSearch(self):
        popup_close = ClosePopups(self.driver) 
        popup_close.click_welcome_button()
        popup_close.click_cookie_button()
        time.sleep(2)
        search_icon = self.driver.find_element(By.CLASS_NAME, "mat-search_icon-search")  
        search_icon.click()
        search_input_field = self.driver.find_element(By.CLASS_NAME, "mat-input-element") 
        search_input_field.send_keys("apple")
        search_input_field.send_keys(Keys.ENTER) 
        time.sleep(5)
        wait = WebDriverWait(self.driver, 10) 
        wait.until(EC.visibility_of_element_located((By.ID, "searchValue")))
        search_results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='item-name']")))
        expected_results = ["Apple Juice (1000ml)", "Apple Pomace"]
        count = 0
        for result in search_results:
            result_text = result.text.strip()
            if result_text in expected_results:
                count += 1
        self.assertEqual(count, len(expected_results))

    def test_02SearchNonExistentElement(self):
        time.sleep(2)
        search_icon = self.driver.find_element(By.CLASS_NAME, "mat-search_icon-search")  
        search_icon.click()
        search_input_field = self.driver.find_element(By.CLASS_NAME, "mat-input-element") 
        search_input_field.send_keys("lollipop")
        search_input_field.send_keys(Keys.ENTER) 
        time.sleep(5)
        wait = WebDriverWait(self.driver, 10) 
        wait.until(EC.visibility_of_element_located((By.ID, "searchValue")))
        no_result_img = self.driver.find_element(By.CLASS_NAME, "noResult")
        assert no_result_img.is_displayed()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))


    


