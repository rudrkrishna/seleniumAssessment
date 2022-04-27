from src.Utils.loctors import ProfilePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage(ProfilePageLocators):

    def __init__(self, driver):
        self.driver = driver

    def manageAddress(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.MANAGE)))
        return element

    def addNewAddress(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ADD_NEW_ADDRESS)))
        return element

    def addName(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.NAME)))
        return element

    def addMobile(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.PHONE)))
        return element

    def addPin(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.PINCODE)))
        return element

    def addlocality(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.LOCALITY)))
        return element

    def addAddr(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ADDRESS)))
        return element

    def selectAddrType(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.ADDRESS_TYPE)))
        return element
    def saveAddr(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.SAVE_BUTTON)))
        return element