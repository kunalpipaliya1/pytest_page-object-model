
from selenium.webdriver.common.by import By
from POM_21062025.locator.Locator import locate

class loginpage():

    username_in = locate.Username_xpath
    password_in = locate.Password_xpath
    login_in = locate.Submitbutton_xpath
    
    def __init__(self,driver):
        self.driver = driver

    def get_username(self,username):
        self.driver.find_element(By.XPATH, self.username_in).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH, self.password_in).send_keys(password)
    
    def presssubmit(self):
        self.driver.find_element(By.XPATH, self.login_in).click()


