from src.Utils.Screenshot import SS
from src.Utils.commonFunc import CommFun
from src.Pages.HomePage import HomePage
from src.Utils.loggingTest import customlogs
from src.Utils.ExcelFileRead import ExcelFileRead

class TestSignInPage(HomePage, CommFun):
    log = customlogs().customLogger()

    def __init__(self, driver):
        self.driver = driver
        self.CommonFun = CommFun(self.driver)
        self.exceldata = ExcelFileRead()

    # Method to enter username
    def userName(self):
       self.CommonFun.sendkeys(self.exceldata.getvalue("username"), self.EnterUserName())

    # Method to enter Password
    def passwordEnter(self):
        self.CommonFun.sendkeys(self.exceldata.getvalue("password"), self.EnterPassword())

    # Method to click submit button
    def submit(self):
        self.CommonFun.JSClick(self.clickLoginButton())
        self.log.info("Login Attempted")

    # Method to verify Login Status
    def verifyMessage(self):
        try:
            print(self.verifyFailMessage())

        except:
            print("Login Successful")
            self.log.info("Login Successful")

    # method to take screenshot and wait for grocery page to load
    def grocerystore(self):
        SS(self.driver).ScreenShot("HomePage.png")
        self.CommonFun.fun_click(self.GroceryOption())
        self.CommonFun.fun_click(self.GroceryPageVerify())
        SS(self.driver).ScreenShot("GroceryStore.png")









