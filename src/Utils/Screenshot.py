import os

from selenium import webdriver

from src.Utils.loggingTest import customlogs


class SS:
    log = customlogs().customLogger()

    # parameterized constructor for Screenshot class
    def __init__(self, driver):
        self.driver = driver

    # method to take screenshot and save to a particular directory
    def ScreenShot(self, path):
        directory = "/Users/rudrkrishna/PycharmProjects/seleniumAssessment/src/Reports/Screenshots/"
        self.driver.get_screenshot_as_file(directory + path)
        self.log.info(path + " Screenshot captured")
