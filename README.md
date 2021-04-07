# PythonSeleniumWebScrapproject
This is a selenium python framework(pytest) end to end to automate webscraping using selenium
* At first it will visit a e com site, 
* Search for a given product and price on first page only, 
* Create two lists one for product and other for their price,
* Create another tuple extracted from both lists
* Saves extracted data in to excel sheet,
* Saves  excel sheet on given location after changing excel sheet name 
* An email templates will create and attched the excel sheet
* Finally will sedn to given email addresses
* Second stage - It will login to email and confirm if the email is sent successfully

## SetUp Instructions
1. [Python selenium installation with pycharm](https://www.javatpoint.com/selenium-python)
2. [Import the project folder from GITHUB](https://stackoverflow.com/questions/41023928/import-github-repository-to-pycharm)
3. To run the test, Go to pycharm terminal and enter - pytest -v --html=Reports//report.html --self-contained-html  -v

### Note
* Please Go to config.py file under Configurations directory and supply your data
* Open pyvenv.cfg file, edit Home and point to your loacal machine where python is up and running
