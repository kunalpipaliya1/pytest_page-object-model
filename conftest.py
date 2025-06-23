import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    driver.implicitly_wait(5)

    yield driver
    driver.quit()
