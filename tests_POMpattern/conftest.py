import pytest as pytest
from selenium import webdriver
@pytest.fixture(scope='class')
def setup(request):
    global driver
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get('https://accounts.shopify.com/signup?rid=dbc83c4e-6fa8-45fb-a6c3-af6963dc6515')
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
@pytest.fixture(scope='class')
def setupHome(request):
    global driver
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get('https://www.shopify.com/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope='class')
def testdata():
    return ("Sindhu","MN","sindhu.suprith@gmail.com","dummy1234@@","dummy1234@@")

@pytest.fixture(scope='class')
def testdata_forfreetrail():
    return ("sindhu.suprith@gmail.com")