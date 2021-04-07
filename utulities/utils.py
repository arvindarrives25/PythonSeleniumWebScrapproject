import time

from openpyxl import Workbook
import smtplib
from email.message import EmailMessage
from Configurations.config import TestData

wb = Workbook()
msg = EmailMessage()
msg['Subject'] = TestData.EMAIL_SUBJECT
msg['From'] = TestData.EMAIL_FROM
msg['To'] = TestData.EMAIL_T0


class Utilities:

    """This method will read the product and prices, save then in list and iterate them
    It will all change the sheet name(as user input)
    It will also create create column names in excel sheet
    Finally it will save the extracted data in to excel sheet and save it"""
    def get_scrap_data(self, locator1, locator2):
        self.is_not_used()
        product_list = []
        price_list = []
        product = locator1
        for prod in product:
            product_list.append(prod.text)
        time.sleep(2)
        price = locator2
        for pri in price:
            price_list.append(pri.text)
        time.sleep(2)
        wb['Sheet'].title = TestData.SHEET_TITLE
        sh1 = wb.active
        sh1.append([TestData.COLUMN_TITLE1, TestData.COLUMN_TITLE2])
        for x in zip(product_list, price_list):
            sh1.append(x)

        wb.save(TestData.SCRAP_DATA_PATH)

    """This method will read standard email template that we want to send
    Email template is customizable """
    def email_template(self):
        self.is_not_used()
        with open(TestData.EMAIL_Template) as my_file:
            message_body = my_file.read()
            msg.set_content(message_body)

    """This method will attach the excel file consists of data in to the email"""
    def email_attachment(self):
        self.is_not_used()
        with open(TestData.SCRAP_DATA_PATH, 'rb') as excel_file:
            excel_data = excel_file.read()
            excel_name = excel_file.name
            msg.add_attachment(excel_data, maintype="webscrapping", subtype="xlsx", filename=excel_name)

    """This method will initialize mail serve and port number, also will user name and password of the sender
     and finally will send the email"""
    def email_server(self):
        self.is_not_used()
        with smtplib.SMTP_SSL(TestData.EMAIL_SERVER, TestData.EMAIL_PORT) as mail_server:
            mail_server.login(TestData.EMAIL_SENDER, TestData.EMAIL_PASSWORD)
            mail_server.send_message(msg)

    """This method is to remove warning and i don't user it as a static class,
    Second work around would be just use @static decorator"""
    def is_not_used(self):
        pass
