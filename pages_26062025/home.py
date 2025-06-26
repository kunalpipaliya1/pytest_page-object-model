from selenium.webdriver.common.by import By
from POM_26062025.Locator.locator import Locate
from selenium.webdriver.common.keys import Keys

class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def PIMcli(self):
        self.driver.find_element(By.XPATH, Locate.Add_emp_xpath).click()

    def Addbutton(self):
        self.driver.find_element(By.XPATH, Locate.Add_plus_xpath).click()

    def add_first_name(self, first):
        Fname = self.driver.find_element(By.NAME, Locate.First_name)
        Fname.clear()
        Fname.send_keys(first)
        print("After send key first name: " + Fname.get_attribute("value"))


    def add_middle_name(self, middle):
        mname = self.driver.find_element(By.NAME, Locate.middle_name)
        mname.clear()
        mname.send_keys(middle)
        print("After send key middle name: " + mname.get_attribute("value"))


    def add_last_name(self, last):
        lname = self.driver.find_element(By.NAME, Locate.last_name)
        lname.clear()
        lname.send_keys(last)
        print("After send key last name: " + lname.get_attribute("value"))

    
    def empnonew(self, emp):
        empno = self.driver.find_element(By.XPATH, Locate.empl_xpath)
        empno.click()
        print("Before clear emp number: " + empno.get_attribute("value"))

        empno.send_keys(Keys.CONTROL + 'a')
        empno.send_keys(Keys.DELETE)
        print("Before send key emp number: " + empno.get_attribute("value"))

        empno.send_keys(emp)
        print("After send key emp number: " + empno.get_attribute("value"))


    def clicksave(self):
        self.driver.find_element(By.XPATH, Locate.empl_save_xpath).click()

    def Searchbutton_xpath(self):
        self.driver.find_element(By.XPATH, Locate.Search_xpath).click()
