import pytest
from selenium.webdriver.common.by import By

from PageObjects.ShopifyHomePage import ShopifyHomePage


@pytest.mark.usefixtures("setupHome")
class Test0ne:

    def test_TC02_ShopifyHomePage_EmailAddress_ForFreeTrail(self):
        shopifyhomepage1 = ShopifyHomePage(self.driver)
        email=shopifyhomepage1.getEmailAddress_ForFreeTrail().send_keys("Sindhu.suprith@gmail.com")


    def test_TC01_ShopifyHomepage_LoginButton(self):
        shopifyhomepage=ShopifyHomePage(self.driver)
        shopifyhomepage.LogInButton()


