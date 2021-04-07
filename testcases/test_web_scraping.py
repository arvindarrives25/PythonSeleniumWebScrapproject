from Configurations.config import TestData
from pageobjects.webscrap_page import WebScrapPage
from testcases.test_base import TestBase


class TestWebScraping(TestBase):
    log = TestBase.get_logger()

    """Test case for extracting data from webpage, saving in excel and sending email with attachment"""
    # This test case fetch only first page data, if you want data from all pages then scroll till then end and fetch
    def test_web_scraping(self):
        self.log.info("Creating object of WebScrapPage class")
        self.object = WebScrapPage(self.driver)
        self.log.info("launching E-com site and searching for desired product")
        self.object.do_search(TestData.WEB_SEARCH_TEXT, TestData.WEB_URL)
        self.log.info("Fetching data from site and saving into excel sheet")
        self.object.get_data()
        self.log.info("Sending email with attached excel sheet(having scrapped data")
        self.object.send_email()
        self.log.info("Logging in Receivers email")
        self.object.do_login_email(TestData.EMAIL_URL, TestData.USERNAME, TestData.PASSWORD)
        self.log.info("Searching for email having attached excel sheet")
        actual_email_subject = self.object.get_email_sub_heading(TestData.EMAIL_SUBJECT)
        self.log.info("Checking if email is visible and expected email subject to actual email subject")
        assert actual_email_subject == TestData.EMAIL_SUBJECT, self.log.error("Scraped data email attachment is not "
                                                                              "visible, Test case failed")
        self.log.info("Scraped data(excel sheet) email attachment sent and received successfully, hence Test case "
                      "passed")
        self.log.info("Email received with attachment(with scrapped data, hence Test case passed")
        self.log.info("Yay! our end to end workflow is working :)")
