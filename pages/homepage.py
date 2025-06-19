from selenium.webdriver.common.by import By
from Selenium_Test.Locator.locator import locate

class Homepage():

    def __init__(self, driver):
        self.driver = driver
        self.webportal_xpath = locate.webportal_xpath
        self.Logout_classname = locate.Logout_classname


    def clickoperation_webportal(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.webportal_xpath).click()

    def clickoperation_logout(self):
        driver = self.driver
        driver.find_element(By.CLASS_NAME, self.Logout_classname).click()