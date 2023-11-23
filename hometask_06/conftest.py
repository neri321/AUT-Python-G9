import pytest
from selenium import webdriver


@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()  # setup
    yield driver
    driver.quit()  # teardown
