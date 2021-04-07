from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage
from utulities.utils import Utilities


class WebScrapPage(BasePage):
    text_search_box = (By.XPATH, "//*[@class='SearchBox']/div/input")
    list_product = (By.XPATH, "//*[@class='m-content__product-list__title']/h2")
    list_product_price = (By.XPATH, "//*[@class='price-info']")
    product_locator = "//*[@class='m-content__product-list__title']/h2/span"
    price_locator = "//*[@class='price-info']/span[2]/span"

    """G-Mail details"""
    text_username = (By.XPATH, "//input[@type='email']")
    btn_next_user = (By.XPATH, "//*[@id='identifierNext']/div/button/div[2]")
    text_password = (By.XPATH, "//input[@type='password']")
    btn_next_psd = (By.XPATH, "//*[@id='passwordNext']/div/button/div[2]")
    text_email_subject = (By.XPATH, "//*[@id=':2m']")

    def __init__(self, driver):
        super().__init__(driver)
        self.obj2 = Utilities()

    """This method will return the title of the login page"""
    def do_search(self, text, url):
        self.driver.get(url)
        self.driver.maximize_window()
        return self.do_send_keys_and_enter(self.text_search_box, text)

    """This method will extract data from webpage and will save in excel sheet and will save it"""
    def get_data(self):
        self.obj2.get_scrap_data(self.driver.find_elements_by_xpath(self.product_locator),
                                 self.driver.find_elements_by_xpath(self.price_locator))

    """This method will send an email with attachment"""
    def send_email(self):
        self.obj2.email_template()
        self.obj2.email_attachment()
        self.obj2.email_server()

    """This method will login in to gmail- account"""
    def do_login_email(self, url, user, pwd):
        self.driver.get(url)
        self.driver.maximize_window()
        self.do_send_keys(self.text_username, user)
        self.do_click(self.btn_next_user)
        self.do_send_keys(self.text_password, pwd)
        self.do_click(self.btn_next_psd)

    """This method will true if email received with attachment, else False"""
    def get_email_sub_heading(self, email_sub_text):
        return self.get_text_of_visible_elements(self.text_email_subject, email_sub_text)


