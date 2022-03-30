from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.ShopifyHomePage import ShopifyHomePage


@pytest.mark.usefixtures("setupHome")
class Test0ne:
    @pytest.mark.smoke
    def test_TC01_ShopifyHomepage_LoginButton_navigation_to_signup_page(self):
        shopifyhomepage=ShopifyHomePage(self.driver)
        loginpage=shopifyhomepage.LogInButton()
        getstarted_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME,"commit")))
        assert loginpage.getNextbutton().is_enabled()
        signuppage=loginpage.getStarted()
        sleep(3)
        assert(self.driver.title=="Sign up")




'''
        getstarted_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Get started")))

        self.driver.find_element(By.LINK_TEXT, "Get started").click()
        sleep(10)
'''
