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

    def userName(self):
       self.CommonFun.sendkeys(self.exceldata.getvalue("username"), self.EnterUserName())

    def passwordEnter(self):
        self.CommonFun.sendkeys(self.exceldata.getvalue("password"), self.EnterPassword())

    def submit(self):
        self.CommonFun.JSClick(self.clickLoginButton())
        self.log.info("Login Attempted")
        SS(self.driver).ScreenShot("HomePage.png")


    def verifyMessage(self):
        try:
            print(self.verifyFailMessage())

        except:
            print("Login Successful")
            self.log.info("Login Successful")

    def grocerystore(self):
        self.CommonFun.fun_click(self.GroceryOption())
        SS(self.driver).ScreenShot("GroceryStore.png")






