import pytest
from POM_26062025.pages_26062025.login import Login
from POM_26062025.pages_26062025.home import Homepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='oxd-input oxd-input--active' and @placeholder='Search']")))
        print("Login successful.")

        # Add employee
        HP = Homepage(self.driver)
        HP.PIMcli()
        HP.Addbutton()
        HP.add_first_name("Kunal")
        HP.add_middle_name("V")
        HP.add_last_name("Pipaliya")
        HP.empnonew("0604")
        HP.Searchbutton_xpath()
        wait.until(EC.visibility_of_any_elements_located((By.XPATH, "//input[@class='oxd-input oxd-input--active' and not(@placeholder='Search')]")))

        print("Employee added.")

    def test_validate_function(self):
        HP = Homepage(self.driver)
        HP.PIMcli()
        HP.empnonew("0604")
        HP.Searchbutton_xpath()

        time.sleep(2)
        
        validate_xpath  = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div"
        empl_validate = self.driver.find_element(By.XPATH, validate_xpath).text
        assert "0604" in empl_validate
        print("Employee validation successful.")