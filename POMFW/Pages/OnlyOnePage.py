"""
class mainpage():

    def __init__(self, driver): # Constructor with the argument 'driver'
        self.driver = driver

    # Creating the locators or the objects. We have 4 in our case.
    # In future, if there is a new field or button added, the locator type is changed or anything else,
    # this is the only page where we will have to make the changes accordingly.
        self.addnewquote_button_id = "show-modal"   # object/locator name_type_locator type
        self.authorname_textbox_id = "autorInput"   # object/locator name_type_locator type
        self.quote_textbox_id = "quoteInput"        # object/locator name_type_locator type
        self.save_button_xpath = "/html/body/div/div/div/div[1]/div/div/div/div/div[3]/button[1]"   # object/locator name_type_locator type

    # Creating the action methods
    def click_addnewquote_button(self):
        self.driver.find_element_by_id(self.addnewquote_button_id).click()

    def enter_authorname(self, author):
        self.driver.find_element_by_id(self.authorname_textbox_id).clear() # This is to clear the data from the textbox before we enter
        self.driver.find_element_by_id(self.authorname_textbox_id).send_keys(author)

    def enter_quote(self, quote):
        self.driver.find_element_by_id(self.quote_textbox_id).clear() # This is to clear the data from the textbox before we enter
        self.driver.find_element_by_id(self.quote_textbox_id).send_keys(quote)

    def click_save_button(self):
        self.driver.find_element_by_xpath(self.save_button_xpath).click()

"""
from POMFW.Locators.All_Locators import locators
class mainpage():

    def __init__(self, driver): # Constructor with the argument 'driver'
        self.driver = driver

        self.addnewquote_button_id = locators.addnewquote_button_id   # object/locator name_type_locator type
        self.authorname_textbox_id = locators.authorname_textbox_id   # object/locator name_type_locator type
        self.quote_textbox_id = locators.quote_textbox_id             # object/locator name_type_locator type
        self.save_button_xpath = locators.save_button_xpath           # object/locator name_type_locator type

    # Creating the action methods
    def click_addnewquote_button(self):
        self.driver.find_element_by_id(self.addnewquote_button_id).click()

    def enter_authorname(self, author):
        self.driver.find_element_by_id(self.authorname_textbox_id).clear() # This is to clear the data from the textbox before we enter
        self.driver.find_element_by_id(self.authorname_textbox_id).send_keys(author)

    def enter_quote(self, quote):
        self.driver.find_element_by_id(self.quote_textbox_id).clear() # This is to clear the data from the textbox before we enter
        self.driver.find_element_by_id(self.quote_textbox_id).send_keys(quote)

    def click_save_button(self):
        self.driver.find_element_by_xpath(self.save_button_xpath).click()
