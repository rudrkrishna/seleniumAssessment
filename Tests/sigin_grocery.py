from src.Utils.commonFunc import CommFun
from src.Pages.HomePage import HomePage
from src.Utils.loggingTest import customlogs
from src.Utils.ExcelFileRead import ExcelFileRead

class TestSignInPage(HomePage, CommFun, ):

    def __init__(self, driver):
        self.driver = driver
        self.CommonFun = CommFun(self.driver)
        self.log = customlogs().customLogger()
        self.exceldata = ExcelFileRead()

    def userName(self):
       self.CommonFun.sendkeys(self.exceldata.getvalue("username"), self.EnterUserName())

    def passwordEnter(self):
        self.CommonFun.sendkeys(self.exceldata.getvalue("password"), self.EnterPassword())

    def submit(self):
        self.CommonFun.JSClick(self.clickLoginButton())
        self.log.info("Login Attempted")

    def verifyMessage(self):
        try:
            print(self.verifyFailMessage())

        except:
            print("Login Successful")
            self.log.info("Login Successful")

    def grocerystore(self):
        self.CommonFun.fun_click(self.GroceryOption())






