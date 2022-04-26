from selenium.webdriver import Keys

from src.Pages.GroceryPage import GroceryPage
from src.Utils.commonFunc import CommFun
from src.Utils.loggingTest import customlogs

class TestCart(GroceryPage, CommFun):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.CommonFun = CommFun(self.driver)
        self.log = customlogs().customLogger()

    def itemSearch(self, value):
        self.CommonFun.sendkeysenter(value, self.searchItems())
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(10)

    def addtocart1(self):
        self.CommonFun.JSClick(self.add1stitem())

    def addtocart2(self):
        self.CommonFun.JSClick(self.add1stitem())

    def addtocart3(self):
        self.CommonFun.JSClick(self.add1stitem())

    def cartClick(self):
        self.CommonFun.JSClick(self.cartbuttonclick())


    def cartVerify(self):
        if "Grocery" in self.CommonFun.verifyText(self.cartProductVerify()):
            self.log.info("Items added in the cart are verified")
            print("Items added in the cart are verified")
        else:
            self.log.warning("Items not added to the cart")
            raise Exception("Items not added to the cart")

