from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.Utils.loctors import SearchPageLocators


class ProductFilter(SearchPageLocators):

    def __init__(self, driver):
        self.driver = driver

    # method which returns searchbox webelement
    def searchItems(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.SEARCH_ITEM)))
        return element

    # method which returns Brand checkbox webelement in filter
    def selectBrand(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.BRAND_SELECT)))
        return element

    # method which returns Name of the brand webelement
    def getBrandName(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.BRAND_NAME)))
        return element

    # method which returns resultant product webelement
    def verifyProduct(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.BRAND_VERIFY)))
        return element

    # method which returns Homepage icon webelement
    def NavigateToHome(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.HOME_PAGE)))
        return element
