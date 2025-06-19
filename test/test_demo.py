from selenium import webdriver
from Selenium_Test.pages.loginpage import Loginpage
from Selenium_Test.pages.homepage import Homepage
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Testdemo:

    @pytest.fixture()
    def setup_teardown(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(5)
        yield driver
        driver.quit()
        print("POM Test Completed")

    
    def test_loginpage(self,setup_teardown):
        driver = setup_teardown
        
        lp = Loginpage(driver)
        lp.ENTERFIRSTNAME("Admin")
        lp.ENTERPASSWORD("admin123")
        lp.CLICK_LOGIN()

        assert "OrangeHRM" in driver.title
        print("Title is verified")

        hp = Homepage(driver)
        hp.clickoperation_webportal()
        hp.clickoperation_logout()

        
