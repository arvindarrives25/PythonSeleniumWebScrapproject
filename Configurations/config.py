class TestData:

    EXPLICIT_WAIT = 15
    """URL and product name from where we want to fetch data"""
    WEB_URL = "https://www.nykaa.com/"
    WEB_SEARCH_TEXT = "Lakme"

    EMAIL_SUBJECT = "Nyka - Lakme product with price list"
    EMAIL_FROM = "Test - Automation"
    """Please add receivers email address """
    EMAIL_T0 = "sample.email1.com, sample.email2.com"
    EMAIL_Template = "Configurations/email_template.txt"

    """Email server details"""
    EMAIL_SERVER = 'smtp.gmail.com'
    EMAIL_PORT = 465
    """Please set email and password from which toy want to send"""
    EMAIL_SENDER = 'your.email@gmail.com'
    EMAIL_PASSWORD = '#########'

    """Path where we want to save data"""
    SCRAP_DATA_PATH = "Configurations/NykaLakmeProductPriceList.xlsx"

    """Excel sheet name, product column and price column """
    SHEET_TITLE = 'NykaLakme'
    COLUMN_TITLE1 = 'Product'
    COLUMN_TITLE2 = 'Price'

    """Receivers email details """
    EMAIL_URL = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F" \
                "&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin "
    """Please enter email and password, where you want to check if email received, for example you can send yourself 
    and check """
    USERNAME = "************"
    PASSWORD = "############"

    EMAIL_EXP_SUB_HEADING = "Nyka - Lakme product with price list"
