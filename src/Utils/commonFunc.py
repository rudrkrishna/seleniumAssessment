import logging
import os
import time

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CommFun:

    def __init__(self, driver):
        self.driver = driver

    def fun_click(self, WebElement):
        try:
            self.Fluentwait(WebElement)
            WebElement.click()
            return True

        except:
            #self.log.info("Element is not clicked")
            return False

    def sendkeys(self, data, WebElement):
        try:
            self.Fluentwait(WebElement)
            WebElement.clear()
            WebElement.send_keys(data)
            return True

        except:
            #self.log.info("Value are not entered")
            return False

    def findWebElement(self, locator):

        WebElement = self.driver.find_element(By.XPATH, locator)
        return True

    def Fluentwait(self, WebElement):

        try:
            wait = WebDriverWait(self.driver, 25, poll_frequency=2,
                                 ignored_exceptions=[ElementNotVisibleException, StaleElementReferenceException,
                                                     NoSuchElementException])
            webElement = wait.until(EC.presence_of_element_located(WebElement))
            return webElement
        except:
            # self.log.info("Element is not present in the page")
            return False

    def capturescreenshot(self, resultMessage, TestCaseID):
        try:
            filename = TestCaseID + "_" + resultMessage + "_" + ".png"
            destination_location = self.constants.ScreenshotPath + filename
            self.driver.save_screenshot(destination_location)

            return True
        except:
            #self.log.info("Screenprint is not taken")
            return False

    def CheckBoxSelection(self, WebElemet, value):
        try:
            checkBox = self.driver.find_element(By.XPATH, WebElemet)
            checkBox.click()
            return True
        except:
            #self.log.info("CheckBox is not selected")
            return False

    def RadioButtonSelection(self, WebElemet, value):
        try:
            RadioButtonSelection = self.driver.find_element(By.XPATH, WebElemet)
            RadioButtonSelection.click()
            return True
        except:
            #self.log.info("RadioButtonSelection is not selected")
            return False

    def JSClick(self,WebElement):
        try:
            self.Fluentwait(WebElement)
            self.driver.execute_script('arguments[0].scrollIntoView(true);', WebElement)
            self.driver.execute_script("arguments[0].click();", WebElement)

            return True
        except:
            #self.log.info("Element is not clicked")
            return False

    def pagewaitTime(self):
        self.driver.set_page_load_timeout(10)


    def verifyText(self, webelement):
        return webelement.text

    def implicitwait(self):
        self.driver.implicitly_wait(10)

    def sendkeysenter(self, data, WebElement):
        try:
            self.Fluentwait(WebElement)
            WebElement.clear()
            WebElement.send_keys(data, Keys.ENTER)
            return True

        except:
            #self.log.info("Value are not entered")
            return False

