# Data Driven Testing to load all the quotes of Gideon to our website's data baase

import XLUtils
from selenium import webdriver
import time

driver = webdriver.Chrome("E:/Madhu Chandra K/Software Testing/Test Automation/chromedriver.exe")
driver.implicitly_wait(2)
# driver.maximize_window()

driver.get("https://www-5d9f3c97e4fb4f546e733d76.recruit.eb7.io")

path = "C:/Users/madhu/Desktop/e-bot7/Gideon_Quotes.xlsx"   # Path of the excel file which has the Gideon quotes

rows = XLUtils.getRowCount(path,'Quotes_by_Gideon')

for r in range(2, rows+1):
    author = XLUtils.readData(path, 'Quotes_by_Gideon', r, 1)
    quote = XLUtils.readData(path, 'Quotes_by_Gideon', r, 2)

    driver.find_element_by_id("show-modal").click()
    driver.find_element_by_id("autorInput").send_keys(author)
    driver.find_element_by_id("quoteInput").send_keys(quote)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div[3]/button[1]").click()
    driver.implicitly_wait(5)

    if driver.title == "e-bot7 - Sandbox":
        print("Test is a pass")
        XLUtils.writeData(path, 'Quotes_by_Gideon', r, 3, "Quote added successfully")
    else:
        print("Test is a fail")
        XLUtils.writeData(path, 'Quotes_by_Gideon', r, 3, "Quote was not added")

    driver.implicitly_wait(10)

time.sleep(2)
driver.close()
driver.quit()
print("Done")