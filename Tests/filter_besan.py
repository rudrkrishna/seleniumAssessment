from src.Pages.FilterPage import ProductFilter
from src.Utils.commonFunc import CommFun
from src.Utils.loggingTest import customlogs
from src.Utils.ExcelFileRead import ExcelFileRead


class Test_filter(ProductFilter, CommFun):

    log = customlogs().customLogger()
    exceldata = ExcelFileRead()
    searchData = exceldata.getvalue("filtertest")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.CommonFun = CommFun(self.driver)


    def itemSearch(self, value):
        self.CommonFun.sendkeysenter(value, self.searchItems())
        self.log.info(self.searchData+" Item Searched")

    def setfilter(self):
        self.CommonFun.JSClick(self.selectBrand())
        self.log.info("Filter Applied")

    def verifyFilter(self):
        brandname = self.CommonFun.gettext(self.getBrandName())
        brandresult = self.CommonFun.gettext(self.verifyProduct())
        if brandname in brandresult:
            self.log.info("Filter Verification Successful")
        else:
            self.log.error("Filter not working properly")

    def gotoHomePage(self):
        self.CommonFun.fun_click(self.NavigateToHome())