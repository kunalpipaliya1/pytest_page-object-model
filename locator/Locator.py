class locate():

    # https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

    # Login page
    Username_xpath = "//*[@name='username']"
    Password_xpath = "//*[@name='password']"
    Submitbutton_xpath = "//*[@type='submit']"

    # Homepage validate
    Click_Admin_xpath = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span" # click operation
    Home_username_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input" # class name
    Home_search = "button[type='submit']" # css selector

    # Logout
    Logout_web = "oxd-userdropdown-name" # class name
    Logout_click = "Logout" # link text

