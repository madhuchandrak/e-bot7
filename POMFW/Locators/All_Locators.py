"""
In this website, there is only one page to work on.
However, in websites with numerous pages, we will definitely have numerous objects and their locators
So, all the objects of the entire website can be added in a separate class or a document called 'All_Locators', as shown below

"""

class locators():
    # Our only web page's locators
    addnewquote_button_id = "show-modal"
    authorname_textbox_id = "autorInput"
    quote_textbox_id = "quoteInput"
    save_button_xpath = "/html/body/div/div/div/div[1]/div/div/div/div/div[3]/button[1]"