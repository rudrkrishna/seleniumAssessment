from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.Utils.Screenshot import SS
from src.Utils.loctors import HomePageLocators
from src.Utils.commonFunc import CommFun


class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.CommonFun = CommFun(self.driver)

    def EnterUserName(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.EMAIL)))
        return element

    def EnterPassword(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.PASSWORD)))
        return element

    def clickLoginButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.SUBMIT)))
        return element

    def verifyFailMessage(self):
        try:
            WebElement = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ERRORMESSAGE)))
            self.log.error("Login Failed")
            SS(self.driver).ScreenShot("Loginfailed.png")
        except:
            self.log.info("Login Successful")

    def GroceryOption(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.GROCERY)))
        return element
    def GroceryPageVerify(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.GROCERYLOGO)))
        return element







