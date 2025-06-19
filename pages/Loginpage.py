from POM_19062025.locator.locate import locator
from selenium.webdriver.common.by import By
class loginpage():

    enterfirstname = locator.Firstname_xpath
    enter_last = locator.Lastname_xpath
    enter_email = locator.Email_xpath
    enter_phone = locator.Phone_xpath
    enter_gender = locator.Gender_xpath

    def __init__(self, driver):
        self.driver = driver

    def fname(self, first):
        self.driver.find_element(By.XPATH, self.enterfirstname).clear()
        self.driver.find_element(By.XPATH, self.enterfirstname).send_keys(first)

    def lname(self, last):
        self.driver.find_element(By.XPATH, self.enter_last).clear()
        self.driver.find_element(By.XPATH, self.enter_last).send_keys(last)
    
    def email(self, emailid):
        self.driver.find_element(By.XPATH, self.enter_email).clear()
        self.driver.find_element(By.XPATH, self.enter_email).send_keys(emailid)
    
    def phoone(self, mobile):
        self.driver.find_element(By.XPATH, self.enter_phone).clear()
        self.driver.find_element(By.XPATH, self.enter_phone).send_keys(mobile)

    def gendeer(self):
        self.driver.find_element(By.XPATH, self.enter_gender).click()
    

