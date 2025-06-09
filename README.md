# Step: 1
# ----- Installation library -----
# selenium - selenium library
# pytest - Pythn unit test framwork
# pytest-html - Pytest HTML Report
# pytest-xdist - Run test parallel
# Openpyxl - MS Excel support
# Allure-report - to generate allure reports

# Step: 2
# Create Folder structure

# Project Name
    # |
    # PageObjects(Package)
    # |
    # testCases(Package)
    # |
    # utilities(Package)
    # |
    # TestData(Folder)
    # |
    # Configurations(Folder)
    # |
    # Logs(Folder)
    # |
    # Screenshots(Folder)
    # |
    # Reports(Folder)

# Step: 3
# Automating login test
# Create Loginpage object class under "pageObjects"
# Create LoginTest under "testCases"
# Create "conftest.py" under "testCases"

# command line for execute the test cases.
**
# pytest -v -s test_LoginTest.py --html=Reports/test.html # generate the html report
# pytest -v -s test_LoginTest.py --browser Chrome # Chrome browser launch
# pytest -v -s test_LoginTest.py --browser Firefox # Firefox browser launch
# pytest -v -s -n 2 test_LoginTest.py --browser Firefox # parallel test execution
# pip install pytest-order # to priority to execute code
# pip install pytest-repeat # to Invocation Count	repeat how much time**

