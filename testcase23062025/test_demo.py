import pytest
from POM_23062025.pages_23062025.login import Login
from POM_23062025.pages_23062025.home import Homepage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Test_001_Login:

    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def test_launch_url(self):
        self.driver.get(self.baseURL)
        print("URL is launched...!!!")
    
        LP = Login(self.driver)
        LP.add_username("Admin")
        LP.add_password("admin123")
        LP.login_click()
    
        assert "OrangeHRM" in self.driver.title
        print("Login successful.")

        # Add employee
        HP = Homepage(self.driver)
        HP.PIMcli()
        HP.Addbutton()
        HP.add_first_name("Kunal")
        HP.add_middle_name("V")
        HP.add_last_name("Pipaliya")
        HP.empnonew_clear()
        HP.empnonew("0604")
        HP.Searchbutton_xpath()
        print("Employee added.")

    def test_validate_function(self):
        HP = Homepage(self.driver)
        HP.PIMcli()
        HP.empnonew("0604")
        HP.Searchbutton_xpath()

        validate_xpath  = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div"
        empl_validate = self.driver.find_element(By.XPATH, validate_xpath).text
        assert "0604" in empl_validate
        print("Employee validation successful.")