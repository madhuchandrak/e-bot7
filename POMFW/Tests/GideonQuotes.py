"""
# Plain code

from selenium import webdriver
import time

driver = webdriver.Chrome("E:/Madhu Chandra K/Software Testing/Test Automation/chromedriver.exe")
driver.implicitly_wait(2)
#driver.maximize_window()

driver.get("https://www-5d9f3c97e4fb4f546e733d76.recruit.eb7.io")

driver.find_element_by_id("show-modal").click()
driver.find_element_by_id("autorInput").send_keys("Heraclitus")
driver.find_element_by_id("quoteInput").send_keys("Change is the only constant")
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div[3]/button[1]").click()

time.sleep(2)
driver.close()
driver.quit()
print("Done")

"""

"""
# Python in-built unit test

from selenium import webdriver
import time
import unittest

class Gideon(unittest.TestCase):

    @ classmethod
    def setUpClass(cls): # Will run after all the test methods
        cls.driver = webdriver.Chrome("E:/Madhu Chandra K/Software Testing/Test Automation/chromedriver.exe")
        cls.driver.implicitly_wait(2)

    def test_add_Gideon_quotes(self):
        self.driver.get("https://www-5d9f3c97e4fb4f546e733d76.recruit.eb7.io")
        self.driver.find_element_by_id("show-modal").click()
        self.driver.find_element_by_id("autorInput").send_keys("Heraclitus")
        self.driver.find_element_by_id("quoteInput").send_keys("Change is the only constant")
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div[3]/button[1]").click()
        time.sleep(2)

    @ classmethod
    def tearDownClass(cls): # Will run only once after all the tests are completed. Here the only test to run in test_add_Gideon_quotes
        cls.driver.close()
        cls.driver.quit()
        print("Done")

"""


# Page Object Model implementation
# Identify all objects and actions methods on the page and create a class for each page. In our case, only one web page.

from selenium import webdriver
import time
import unittest
import sys # To run this code from the command or terminal window instead of the PyCharm IDE
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMFW.Pages.OnlyOnePage import mainpage
import HtmlTestRunner

class Gideon(unittest.TestCase):

    @ classmethod
    def setUpClass(cls): # Will run after all the test methods
        cls.driver = webdriver.Chrome("E:/Madhu Chandra K/Software Testing/Test Automation/chromedriver.exe")
        cls.driver.implicitly_wait(2)

    def test_add_empty_quote(self): # Defect ID 1: Accepts blank entry as a quote
        driver = self.driver  # This is to avoid using self.driver in all the below lines of code
        driver.get("https://www-5d9f3c97e4fb4f546e733d76.recruit.eb7.io")
        # Creating the object for these classes to use all the functions and variables in our only web page
        page = mainpage(driver)  # 'page' is the variable I have created to access all the methods
        page.click_addnewquote_button()
        page.enter_authorname("Gideon")
        page.enter_quote("")
        # this is an empty quote
        page.click_save_button()
        time.sleep(2)

    def test_add_very_long_quotes(self): # Defect ID 6: Accepts quote with the length more than 200 characters
        driver = self.driver # This is to avoid using self.driver in all the below lines of code
        driver.get("https://www-5d9f3c97e4fb4f546e733d76.recruit.eb7.io")

    # Creating the object for these classes to use all the functions and variables in our only web page
        page = mainpage(driver) # 'page' is the variable I have created to access all the methods
        page.click_addnewquote_button()
        page.enter_authorname("Gideon")
        page.enter_quote("There are certain clues at a crime scene which, by their very nature, do not lend themselves to being collected or examined.  How does one collect love, rage, hatred, fear…?  These are things that we’re trained to look for.")
        # this quote is 225 characters long with spaces
        page.click_save_button()
        time.sleep(2)

    @ classmethod
    def tearDownClass(cls): # Will run only once after all the tests are completed. Here the only test to run in test_add_Gideon_quotes
        cls.driver.close()
        cls.driver.quit()
        print("Done")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/madhu/PycharmProjects/e-bot7/POMFW/Test Report'))