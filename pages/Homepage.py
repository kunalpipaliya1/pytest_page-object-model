from selenium.webdriver.common.by import By
from POM_21062025.locator.Locator import locate


class homepage():

    adminclick = locate.Click_Admin_xpath
    Home_username = locate.Home_username_xpath
    search_ope = locate.Home_search

    def __init__(self, driver):
        self.driver = driver
    
    def clickoperationper(self):
        self.driver.find_element(By.XPATH, self.adminclick).click()
    
    def enter_username(self,user_na):
        self.driver.find_element(By.XPATH, self.Home_username).send_keys(user_na)
    
    def click_search(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_ope).click()