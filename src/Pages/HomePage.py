from selenium.webdriver.common.by import By

from src.Utils.loctors import HomePageLocators
from src.Utils.commonFunc import CommFun


class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.CommonFun = CommFun(self.driver)

    def EnterUserName(self):
        return self.driver.find_element(By.XPATH, self.EMAIL)

    def EnterPassword(self):
        return self.driver.find_element(By.XPATH, self.PASSWORD)

    def clickLoginButton(self):
        return self.driver.find_element(By.XPATH, self.SUBMIT)

    def verifyFailMessage(self):
        WebElement = self.driver.find_element(By.XPATH, self.ERRORMESSAGE)
        self.CommonFun.Fluentwait(WebElement)
        return self.driver.find_element(self.ERRORMESSAGE).text
    def GroceryOption(self):
        return self.driver.find_element(By.XPATH, self.GROCERY)







