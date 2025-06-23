from selenium.webdriver.common.by import By
from POM_23062025.Locator.locator import Locate

class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def PIMcli(self):
        self.driver.find_element(By.XPATH, Locate.Add_emp_xpath).click()

    def Addbutton(self):
        self.driver.find_element(By.XPATH, Locate.Add_plus_xpath).click()

    def add_first_name(self, first):
        self.driver.find_element(By.NAME, Locate.First_name).send_keys(first)

    def add_middle_name(self, middle):
        self.driver.find_element(By.NAME, Locate.middle_name).send_keys(middle)

    def add_last_name(self, last):
        self.driver.find_element(By.NAME, Locate.last_name).send_keys(last)

    def empnonew_clear(self):
        self.driver.find_element(By.XPATH, Locate.empl_xpath).clear()
    
    def empnonew(self, emp):
        self.driver.find_element(By.XPATH, Locate.empl_xpath).send_keys(emp)

    def clicksave(self):
        self.driver.find_element(By.XPATH, Locate.empl_save_xpath).click()

    def Searchbutton_xpath(self):
        self.driver.find_element(By.XPATH, Locate.Search_xpath).click()
