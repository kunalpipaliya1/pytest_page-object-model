from selenium.webdriver.common.by import By
from Selenium_Test.Locator.locator import locate
class Loginpage():

    def __init__(self, driver):
        self.driver = driver
        self.firstname_xpath= locate.firstname_xpath
        self.password_xpath = locate.password_xpath
        self.login_classname= locate.login_classname
    
    def ENTERFIRSTNAME(self, username):
        self.find_element(By.XPATH, self.firstname_xpath).clear()
        self.find_element(By.XPATH, self.firstname_xpath).send_keys(username)
    
    def ENTERPASSWORD(self, password):
        self.find_element(By.XPATH, self.password_xpath).clear()
        self.find_element(By.XPATH, self.password_xpath).send_keys(password)
    
    def CLICK_LOGIN(self):
        self.find_element(By.CLASS_NAME, self.login_classname).click()
    
