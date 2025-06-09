import pytest
from selenium import webdriver
from pageObjects.LoginPage import login
import time
from utilities.readProperties import ReadConfig
from utilities.logger import LogGen

class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()

    def test_homepageTitle(self, setup): # setup class created inside the "conftest.py"
        self.logger.info("*************Test start************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title, "for test_homepageTitle")

        
        if act_title == "nopCommerce demo store. Login":
            assert True
            self.logger.info("*************Test case passed ************")
            self.driver.close()
        else:
            # self.driver.save_screenshot("./Screenshots/"+"test_homepageTitle.png")
            self.driver.save_screenshot(r"C:\Users\Nmsworks\Documents\KunalLearning\Project\Pytest_Project\Screenshots\test_homepageTitle.png")

            self.driver.close()
            self.logger.error("*************Test case failed ************")

            assert False
            
        
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = login(self.driver) # create object of login page
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()

        time.sleep(10)
        act_title = self.driver.title
        print(act_title, "for test_login")

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*************Test case passed ************")

        else:
            self.driver.save_screenshot(r"C:\Users\Nmsworks\Documents\KunalLearning\Project\Pytest_Project\Screenshots\test_login.png")
            self.driver.close()
            self.logger.error("*************Test case failed ************")
            assert False
            
        




