import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setupHome")
class Test0ne:
    def test_TC01_ShopifyHomepage_LoginButton(self):
        self.driver.find_element(By.LINK_TEXT, 'Log in').click()


