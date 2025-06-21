import pytest
from selenium import webdriver
from POM_21062025.pages.Homepage import homepage
from POM_21062025.pages.Loginpage import loginpage
from POM_21062025.pages.logout import Logout
import time

class Test_00001():

    def test_loginpage(self, setup):
        self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        LP = loginpage(self.driver)
        LP.get_username("Admin")
        LP.enter_password("admin123")
        LP.presssubmit()
        time.sleep(5)

        HP = homepage(self.driver)
        HP.clickoperationper()
        HP.enter_username("Admin")
        HP.click_search()
        time.sleep(5)


        Lout = Logout(self.driver)
        Lout.Logoutweb()
        Lout.Logoutbutton()
        time.sleep(15)

        title = self.driver.title
        assert "OrangeHRM" in title
