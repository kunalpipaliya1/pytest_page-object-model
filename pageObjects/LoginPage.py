from selenium.webdriver.common.by import By

class login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    testbox_login_xpath = "//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    testbox_logout_linktext = "Logout"


    def __init__(self,driver): # It's automatically intial driver
        self.driver = driver

    def setusername(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
    
    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.testbox_login_xpath).click()
    
    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT, self.testbox_logout_linktext).click()


