from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Configurations.config import TestData

""" This class is the parent of all the page classes
    It contains all the custom methods(for example, click(), sendKeys() etc.
"""


class BasePage:
    driver: webdriver.Chrome

    def __init__(self, driver):
        self.driver = driver

    """This is a custom click method, which will wait until the element is visible before clicking """
    def do_click(self, locator):
        try:
            WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(ec.element_to_be_clickable(locator)).click()
        except TimeoutException:
            print("Could not click because locator is not visible : " + str(locator))

    """This method will first clear the input box and then type """
    def do_send_keys(self, locator, text):
        try:
            my_element = WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(ec.element_to_be_clickable(locator))
            my_element.clear()
            my_element.send_keys(text)
        except TimeoutException:
            print("Could not clear or type  because locator is not visible : " + str(locator))

        """This method will first clear the input box and then type """
    def do_send_keys_and_enter(self, locator, text):
        try:
            my_element = WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(
                ec.element_to_be_clickable(locator))
            my_element.clear()
            my_element.send_keys(text)
            my_element.send_keys(Keys.RETURN)
        except TimeoutException:
            print("Could not clear or type  because locator is not visible : " + str(locator))

    """This method will return text of the web element"""
    def get_text(self, locator):
        try:
            my_element = WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(
                ec.visibility_of_element_located(locator))
            return my_element.text
        except TimeoutException:
            print("Could not find the text because locator is not visible : " + str(locator))

    """This method will return if the webElement is visible or not!"""
    def element_visible(self, locator):
        try:
            my_element = WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(
                ec.visibility_of_element_located(locator))
            return bool(my_element)
        except TimeoutException:
            print("Locator is not visible : " + str(locator))

    """This method will return if the WebElement is enabled or not!"""
    def element_enabled(self, locator):
        try:
            my_element = WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(
                ec.visibility_of_element_located(locator))
            return bool(my_element)
        except TimeoutException:
            print("Locator is not enabled: " + str(locator))

    """This method will return title of the page"""
    def get_title(self, title):
        try:
            WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(ec.title_is(title))
            return self.driver.title
        except TimeoutException:
            print("Could not find the Title because its  not visible: ")

    """This method will return if the webElements are visible or not!"""
    def elements_visible(self, locator):
        try:
            my_elements = WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(
                ec.presence_of_all_elements_located(locator))
            for x in my_elements:
                return bool(x)
        except TimeoutException:
            print("Locator is not visible : " + str(locator))

    """This method will return texts of list of web elements"""
    def elements_texts(self, locator):
        try:
            my_elements = WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(
                ec.visibility_of_all_elements_located(locator))
            for x in my_elements:
                return x.text
        except TimeoutException:
            print("Locator is not visible : " + str(locator))

    """This method will return texts of list of web elements, and click on given text"""
    def click_elements_visible(self, locator, my_text):
        try:
            my_elements = WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(
                ec.presence_of_all_elements_located(locator))
            for x in my_elements:
                if x.text == my_text:
                    return x.click()
        except TimeoutException:
            print("Locator is not visible : " + str(locator))

    """This method will return if a specific webElement is visible, if yes then return text of that element"""
    def get_text_of_visible_elements(self, locator, my_text):
        try:
            my_elements = WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(
                ec.presence_of_all_elements_located(locator))
            for x in my_elements:
                if x.text == my_text:
                    return x.text
                else:
                    return False
        except TimeoutException:
            print("Locator is not visible : " + str(locator))
