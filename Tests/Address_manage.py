from src.Utils.commonFunc import CommFun
from src.Utils.loggingTest import customlogs
from src.Utils.ExcelFileRead import ExcelFileRead
from src.Pages.ProfilePage import ProfilePage


class AddressTest(ProfilePage, CommFun):

    log = customlogs().customLogger()
    exceldata = ExcelFileRead()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.CommonFun = CommFun(self.driver)


    def navigateToProfile(self):
        self.driver.get("https://www.flipkart.com/account")
        self.log.info("Navigated to Profile Page")

    def manageAddr(self):
        self.CommonFun.JSClick(self.manageAddress())

    def addNewAddr(self):
        self.CommonFun.fun_click(self.addNewAddress())

    def enterAddress(self):
        self.CommonFun.sendkeys(self.exceldata.getvalue("name"), self.addName())
        self.CommonFun.sendkeys(self.exceldata.getvalue("number"), self.addMobile())
        self.CommonFun.sendkeys(self.exceldata.getvalue("pincode"), self.addPin())
        self.CommonFun.sendkeys(self.exceldata.getvalue("locality"), self.addlocality())
        self.CommonFun.sendkeys(self.exceldata.getvalue("address"), self.addAddr())
        self.CommonFun.RadioButtonSelection(self.selectAddrType())
        self.log.info("Address Entered")

    def saveAddress(self):
        self.CommonFun.fun_click(self.saveAddr())
        self.log.info("Address Saved Successfully")

    def verifySavedAddress(self):
        if str(self.exceldata.getvalue("name")) in self.gettext(self.verifyAddress()):
            self.log.info("Added Address Verified Successfully")
        else:
            self.log.error("Added Address Not verified")

    def logout(self):
        self.CommonFun.fun_click(self.logoutFlipkart())
        self.log.info("Logout Button Clicked")


