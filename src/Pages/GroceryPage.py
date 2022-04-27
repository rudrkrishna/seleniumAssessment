from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.Utils.loctors import GroceryStoreLocators


class GroceryPage(GroceryStoreLocators):

    def __init__(self, driver):
        self.driver = driver

    def searchItems(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.SEARCH)))
        return element


    def searchButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.SEARCHBUTTON)))
        return element


    def add1stitem(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ITEM1)))
        return element

    def add2nditem(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ITEM2)))
        return element


    def add3rditem(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ITEM3)))
        return element

    def cartbuttonclick(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.CART)))
        return element
    def cartProductVerify(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.GROCERYCART)))
        return element






