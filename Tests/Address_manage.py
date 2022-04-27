from src.Utils.commonFunc import CommFun
from src.Utils.loggingTest import customlogs
from src.Utils.ExcelFileRead import ExcelFileRead
from src.Pages.ProfilePage import ProfilePage
import time

# class which have implementation methods of manage address functionality
class AddressTest(ProfilePage, CommFun):

    log = customlogs().customLogger() # logger instance
    exceldata = ExcelFileRead() # excel sheet reader instance

    # parameterized constructor which accepts webdriver instance as input parameter
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.CommonFun = CommFun(self.driver)


    # method to navigate to the profile tab
    def navigateToProfile(self):
        self.driver.get("https://www.flipkart.com/account")
        self.log.info("Navigated to Profile Page")

    # implementation method of manage address clicking action
    def manageAddr(self):
        self.CommonFun.JSClick(self.manageAddress())

    # implementation method of add new address clicking action
    def addNewAddr(self):
        self.CommonFun.fun_click(self.addNewAddress())

    # implementation method of entering address details
    def enterAddress(self):
        self.CommonFun.sendkeys(self.exceldata.getvalue("name"), self.addName())
        self.CommonFun.sendkeys(self.exceldata.getvalue("number"), self.addMobile())
        self.CommonFun.sendkeys(self.exceldata.getvalue("pincode"), self.addPin())
        self.CommonFun.sendkeys(self.exceldata.getvalue("locality"), self.addlocality())
        self.CommonFun.sendkeys(self.exceldata.getvalue("address"), self.addAddr())
        self.CommonFun.RadioButtonSelection(self.selectAddrType())
        self.log.info("Address Entered")

    # implementation method of save address clicking action
    def saveAddress(self):
        self.CommonFun.fun_click(self.saveAddr())
        self.log.info("Address Saved Successfully")

    # implementation method of VERIFYING saved address
    def verifySavedAddress(self):
        if str(self.exceldata.getvalue("name")) in self.gettext(self.verifyAddress()):
            self.log.info("Added Address Verified Successfully")
        else:
            self.log.error("Added Address Not verified")

    # implementation method of logout functionality
    def logout(self):
        self.CommonFun.fun_click(self.logoutFlipkart())
        self.log.info("Logout Button Clicked")
        # static wait added to check whether logout is working or not
        time.sleep(10)


