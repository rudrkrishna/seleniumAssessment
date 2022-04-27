from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.Utils.loctors import SearchPageLocators


class ProductFilter(SearchPageLocators):

    def __init__(self, driver):
        self.driver = driver


    def searchItems(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_ITEM)))
        return element

    def selectBrand(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.BRAND_SELECT)))
        return element

    def getBrandName(self):
        element = WebDriverWait(self.driver, 10).until(EC.staleness_of((By.XPATH, self.BRAND_NAME)))
        return element

    def verifyProduct(self):
        element = WebDriverWait(self.driver, 10).until(EC.staleness_of((By.XPATH, self.BRAND_VERIFY)))
        return element

    def NavigateToHome(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.HOME_PAGE)))
        return element
