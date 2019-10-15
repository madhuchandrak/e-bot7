# Data Driven Testing to load all the quotes of Gideon to our website's data baase

import XLUtils
from selenium import webdriver

# For now I will not use the executable_path to access the Chrome webdriver
driver = webdriver.Chrome("E:/Madhu Chandra K/Software Testing/Test Automation/chromedriver.exe")
driver.implicitly_wait(2)
driver.maximize_window()

driver.get("https://www-5d9f3c97e4fb4f546e733d76.recruit.eb7.io")
driver.find_element_by_id("show-modal").click()

path = "C:/Users/madhu/Desktop/e-bot7/Gideon.xlsx"   # Path of the excel file which has the Gideon quotes

rows=XLUtils.getRowCount(path,'Quotes')

for r in range(2, rows+1):  # As our excel data sheet has only 3 columns we need only one for loop to access the data
    author = XLUtils.readData(path, "Quotes", r, 1)
    quotes = XLUtils.readData(path, "Quotes", r, 2)

    driver.find_element_by_id("autorInput").send_keys(author)
    driver.find_element_by_id("quoteInput").send_keys(quotes)
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div[3]/button[1]").click()

    driver.implicitly_wait(5)

    if driver.title == "e-bot7 - Sandbox": # Since the success message after adding the quote is not displayd at the moment, I am using the title of the page for pass or fail assertion
        print("Test is a pass")
        XLUtils.writeData(path, "Quotes", r, 3, "Quote added successfully") # To update the test result in the 3rd column in the same excel of the test is a pass
    else:
        print("Test is a fail")
        XLUtils.writeData(path, "Quotes", r, 3, "Quote not added") # To update the test result in the 3rd column in the same excel if the test is a fail

    driver.find_element_by_id("show-modal").click() # This is to add the next quote

driver.close()
driver.quit()
print("Test completed")