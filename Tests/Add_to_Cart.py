from selenium.webdriver import Keys

from src.Pages.GroceryPage import GroceryPage
from src.Utils.commonFunc import CommFun
from src.Utils.loggingTest import customlogs
from src.Utils.ExcelFileRead import ExcelFileRead

# class which have implementations of Adding items to cart functionality
class TestCart(GroceryPage, CommFun):

    log = customlogs().customLogger() # logger instance
    exceldata = ExcelFileRead() # excel sheet reader instance

    item1 = exceldata.getvalue("searchitem1") # data fetched from excel sheet
    item2 = exceldata.getvalue("searchitem2") # data fetched from excel sheet
    item3 = exceldata.getvalue("searchitem3") # data fetched from excel sheet

    # parameterized constructor which accepts webdriver instance as input parameter
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.CommonFun = CommFun(self.driver)


    # Implementation method of Item search in Grocery store
    def itemSearch(self, value):
        self.CommonFun.sendkeys(value, self.searchItems())
        self.CommonFun.JSClick(self.searchButton())

    # Implementation method of adding item to cart in Grocery store
    def addtocart1(self):
        self.CommonFun.fun_click(self.add1stitem())

    # Implementation method of adding item to cart in Grocery store
    def addtocart2(self):
        self.CommonFun.fun_click(self.add1stitem())

    # Implementation method of adding item to cart in Grocery store
    def addtocart3(self):
        self.CommonFun.fun_click(self.add1stitem())

    # Implementation method of anavigating to cart
    def cartClick(self):
        self.CommonFun.sendkeys("", self.searchItems())
        self.CommonFun.JSClick(self.cartbuttonclick())

    # Implementation method of cart verifying
    def cartVerify(self):
        if "Grocery" in self.CommonFun.verifyText(self.cartProductVerify()):
            self.log.info("Items added in the cart are verified")
            print("Items added in the cart are verified")
        else:
            self.log.warning("Items not added to the cart")
            raise Exception("Items not added to the cart")

