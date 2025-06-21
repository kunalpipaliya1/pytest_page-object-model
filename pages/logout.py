from POM_21062025.locator.Locator import locate
from selenium.webdriver.common.by import By
class Logout():

    Logoutclickonweb = locate.Logout_web
    Logoutclickonbutton = locate.Logout_click

    def __init__(self, driver):
        self.driver = driver
    
    def Logoutweb(self):
        self.driver.find_element(By.CLASS_NAME, self.Logoutclickonweb).click()

    def Logoutbutton(self):
        self.driver.find_element(By.LINK_TEXT, self.Logoutclickonbutton).click()
