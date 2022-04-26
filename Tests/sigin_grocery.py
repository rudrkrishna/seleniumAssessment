from src.Utils.commonFunc import CommFun
from src.Pages.HomePage import HomePage


class TestSignInPage(HomePage, CommFun):

    def __init__(self, driver):
        self.driver = driver
        self.CommonFun = CommFun(self.driver)

    def userName(self):
       self.CommonFun.sendkeys("9398088298", self.EnterUserName())

    def passwordEnter(self):
        self.CommonFun.sendkeys("Kumar@123", self.EnterPassword())

    def submit(self):
        self.CommonFun.JSClick(self.clickLoginButton())

    # def verifyMessage(self):
    #     try:
    #         self.verifyFailMessage()
    #         print("Enter Valid Credentials")
    #     except:
    #         print("Login Successful")

    def grocerystore(self):
        self.CommonFun.JSClick(self.GroceryOption())






