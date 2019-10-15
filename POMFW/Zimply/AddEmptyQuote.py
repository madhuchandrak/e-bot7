# Add a blank entry without the author name and quote

from selenium import webdriver
import time

driver = webdriver.Chrome("E:/Madhu Chandra K/Software Testing/Test Automation/chromedriver.exe")
driver.implicitly_wait(2)

driver.get("https://www-5d9f3c97e4fb4f546e733d76.recruit.eb7.io")
driver.find_element_by_id("show-modal").click()
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div[3]/button[1]").click()