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


