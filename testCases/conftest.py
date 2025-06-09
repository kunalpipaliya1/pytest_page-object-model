import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="Chrome",
        help="Browser option: Chrome, Firefox, Ie"
    )

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == "Chrome":
        driver = webdriver.Chrome()
        print("Chrome browser launching...")
    elif browser == "Firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox...")
    else:
        driver = webdriver.Ie()
        print("Launching IE browser")
    return driver
