from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        try:
            WebElement = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ERRORMESSAGE)))
            self.log.error("Login Failed")
        except:
            print("Login Successful")
            self.log.error("Login Successful")

    def GroceryOption(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.GROCERY)))
        return element







