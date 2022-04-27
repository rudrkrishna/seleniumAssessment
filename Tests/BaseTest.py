import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.Utils.loggingTest import customlogs

# class which have driver instantiation and teardown methods
class BaseTest:

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.delete_all_cookies()
    driver.maximize_window()
    log = customlogs().customLogger()

    # method which created driver instance and returns the same
    def setUp(self):
        self.driver.get("https://www.flipkart.com/")
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(10)
        self.log.info("Website Launched Successfully")
        return self.driver

    # method which closes aor quits the browser
    def tearDown(self):
        self.driver.quit()
        self.log.info("Driver Closed Successfully")




