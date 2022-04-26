import os

from selenium import webdriver


class SS:

    def __init__(self, driver):
        self.driver = driver

    def ScreenShot(self, path):
        directory = "/Users/rudrkrishna/PycharmProjects/seleniumAssessment/src/Reports/Screenshots/"
        self.driver.get_screenshot_as_file(directory + path)
