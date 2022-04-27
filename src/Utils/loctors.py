from selenium.webdriver.common.by import By

# Object repository of Home page Locators
class HomePageLocators:
    EMAIL = '//div[contains(@class,"row")]//input[@type="text"]'
    PASSWORD = '//div[contains(@class,"row")]//input[@type="password"]'
    Mob= "9398088298"
    Pass= "Kumar@123"
    SUBMIT = '//div[contains(@class,"row")]//button[@type="submit"]//span'
    ERRORMESSAGE = '//span[contains(text(),"incorrect")]'
    GROCERY = '//img[@alt="Grocery"]'
    GROCERYLOGO ='(//a[contains(@href, "GROCERY")])[1]'

# Object repository of Grocery store page Locators
class GroceryStoreLocators:

    SEARCH = '//input[contains(@title,"Search")]'
    SEARCHBUTTON = '//input[contains(@title,"Search")]/../following-sibling::button'
    ITEM1 = '(//button/span[text()="Add Item"])[1]'
    ITEM2 = '(//button/span[text()="Add Item"])[1]'
    ITEM3 = '(//button/span[text()="Add Item"])[1]'
    CART = '//span[text()="Cart"]'
    GROCERYCART = '//span[contains(text(),"Grocery Basket")]'

class SearchPageLocators:
    HOME_PAGE = '//img[@title="Flipkart"]'
    SEARCH_ITEM = '//input[contains(@placeholder, "Search for products")]'
    BRAND_SELECT = '((//input[@type = "checkbox"])[3]/following-sibling::div)[1]'
    BRAND_NAME = '((//input[@type = "checkbox"])[3]/following-sibling::div)[2]'
    BRAND_VERIFY = '((((//input[@type = "checkbox"])[3]/following-sibling::div)[2]' \
                   '/../../../../../../../../../../../div)[2]//a)[4]'

class FashionPageLocators:
    FASHION_LINK = '//img[@alt="Fashion"]'


class ProfilePageLocators:
    MANAGE = '//a/div[contains(text(),"Manage Addresses")]'
    ADD_NEW_ADDRESS = '//div[contains(text(),"ADD A NEW ADDRESS")]'
    NAME = '//input[@name="name"]'
    PHONE ='//input[@name="phone"]'
    PINCODE = '//input[@name="pincode"]'
    LOCALITY = '//input[@name="pincode"]/../following-sibling::div/input'
    ADDRESS = '//textarea[@name="addressLine1"]'
    ADDRESS_TYPE = '(//input[@name="locationTypeTag"]/../div)[1]'
    SAVE_BUTTON = '//button[text()="Save"]'
    ADDRESS_VERIFY = '//span[contains(text(), "Manage Addresses")]/..//div//p/span[contains(text(),"Naruto Uzumaki")]'
    LOGOUT = '//span[text()="Logout"]'

