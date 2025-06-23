class Locate():

    # Login page
    user_xpath = "//input[@placeholder='Username']"
    pass_xpath = "//input[@placeholder='Password']"
    sub_xpath = "//button[@type='submit']"

    # Home page
    Add_emp_xpath = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span"     # Click operation
    Add_plus_xpath = "//button[@type='button' and @class='oxd-button oxd-button--medium oxd-button--secondary']"     # Click operation

    First_name = "firstName"
    middle_name = "middleName"
    last_name = "lastName"

    empl_xpath = "//input[@class='oxd-input oxd-input--active' and not(@placeholder)]"

    empl_save_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"

    Search_xpath = "//button[@type='submit' and @class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"


