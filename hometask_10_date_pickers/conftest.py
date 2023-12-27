import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope='session')
def fixture_1():
    print('Setup')
    yield
    print('Teardown')


@pytest.fixture(scope='class')
def chrome(request):
    driver = Chrome()
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()
