from selenium import webdriver
from POM_23062025.Locator.locator import Locate
from selenium.webdriver.common.by import By

class Login():

    def __init__(self,driver):
        self.driver = driver
    
    # Login page
    def add_username(self, username):
        self.driver.find_element(By.XPATH, Locate.user_xpath).send_keys(username)

    def add_password(self, password):
        self.driver.find_element(By.XPATH, Locate.pass_xpath).send_keys(password)

    def login_click(self):
        self.driver.find_element(By.XPATH, Locate.sub_xpath).click()
