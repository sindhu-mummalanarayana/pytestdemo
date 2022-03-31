import pytest
from selenium.webdriver.common.by import By

from PageObjects.ShopifyHomePage import ShopifyHomePage


@pytest.mark.usefixtures("setupHome")
@pytest.mark.usefixtures("testdata_forfreetrail")
class Test0ne:

    def test_TC02_ShopifyHomePage_EmailAddress_ForFreeTrail(self,testdata_forfreetrail):
        shopifyhomepage1 = ShopifyHomePage(self.driver)
        email=shopifyhomepage1.getEmailAddress_ForFreeTrail().send_keys(testdata_forfreetrail)

    @pytest.mark.smoke
    def test_TC01_ShopifyHomepage_LoginButton(self):
        shopifyhomepage=ShopifyHomePage(self.driver)
        shopifyhomepage.LogInButton()


