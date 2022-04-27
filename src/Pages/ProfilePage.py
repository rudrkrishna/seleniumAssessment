from src.Utils.loctors import ProfilePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage(ProfilePageLocators):

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # method which returns manageaddress button webelement
    def manageAddress(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.MANAGE)))
        return element

    # method which returns add new addrress button webelement
    def addNewAddress(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ADD_NEW_ADDRESS)))
        return element

    # method which returns name field webelement
    def addName(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.NAME)))
        return element

    # method which returns mobile number field webelement
    def addMobile(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.PHONE)))
        return element

    # method which returns pincode field webelement
    def addPin(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.PINCODE)))
        return element

    # method which returns locality field webelement
    def addlocality(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.LOCALITY)))
        return element

    # method which returns address field webelement
    def addAddr(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ADDRESS)))
        return element

    # method which returns address type radio button webelement
    def selectAddrType(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.ADDRESS_TYPE)))
        return element

    # method which returns save address button webelement
    def saveAddr(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.SAVE_BUTTON)))
        return element

    # method which webelement for verifying added address
    def verifyAddress(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.ADDRESS_VERIFY)))
        return element

    # method which returns logout button webelement
    def logoutFlipkart(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.LOGOUT)))
        return element