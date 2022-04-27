from src.Pages.FilterPage import ProductFilter
from src.Utils.commonFunc import CommFun
from src.Utils.loggingTest import customlogs
from src.Utils.ExcelFileRead import ExcelFileRead

# class which have implementation methods of testing the filter in search page
class Test_filter(ProductFilter, CommFun):

    log = customlogs().customLogger() # logger instance
    exceldata = ExcelFileRead() # excel sheet reader instance
    searchData = exceldata.getvalue("filtertest") # getting data from excel sheet

    # parameterized constructor which accepts webdriver instance as input parameter
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.CommonFun = CommFun(self.driver)

    # Implementation method of Item search
    def itemSearch(self, value):
        self.CommonFun.sendkeysenter(value, self.searchItems())
        self.log.info(self.searchData+" Item Searched")

    # Implementation method of filter setting
    def setfilter(self):
        self.CommonFun.JSClick(self.selectBrand())
        self.log.info("Filter Applied")

    # Implementation method of filter verification
    def verifyFilter(self):

        brandname = self.CommonFun.gettext(self.getBrandName())
        brandresult = self.CommonFun.gettext(self.verifyProduct())
        if brandname in brandresult:
            self.log.info("Filter Verification Successful")
        else:
            self.log.error("Filter not working properly")

    # Implementation method navigating to home page
    def gotoHomePage(self):
        self.driver.get("https://www.flipkart.com/")
        self.CommonFun.fun_click(self.NavigateToHome())