from selenium.webdriver.common.by import By
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
        return self.driver.find_element(By.XPATH, self.CART)
    def cartProductVerify(self):
        return self.driver.find_element(By.XPATH, self.GROCERYCART)






