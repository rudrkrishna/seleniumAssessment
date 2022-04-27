from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.Utils.loctors import GroceryStoreLocators


class GroceryPage(GroceryStoreLocators):

    def __init__(self, driver):
        self.driver = driver

    def searchItems(self):
        return self.driver.find_element(By.XPATH, self.SEARCH)

    def searchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCHBUTTON)

    def add1stitem(self):
        return self.driver.find_element(By.XPATH, self.ITEM1)

    def add2nditem(self):
        return self.driver.find_element(By.XPATH, self.ITEM2)

    def add3rditem(self):
        return self.driver.find_element(By.XPATH, self.ITEM3)

    def cartbuttonclick(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.CART)))
        return element
    def cartProductVerify(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.GROCERYCART)))
        return element






