from selenium import webdriver
import pytest
from POM_19062025.pages.Loginpage import loginpage

class TestAutomation():

    @pytest.fixture()
    def loginpage1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://demo.automationtesting.in/Register.html")
        yield driver
        driver.implicitly_wait(20)
        driver.quit()
        print("Test Completed")
    
    def test_registerpage(self, loginpage1):
        driver  = loginpage1
        LP = loginpage(driver)
        LP.fname("Kunal")
        LP.lname("Patel")
        LP.email("abc@gmail.com")
        LP.phoone("+91 8274939393")
        LP.gendeer()

        