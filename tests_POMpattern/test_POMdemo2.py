from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.SignUpPage import SignUpPage


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("testdata")
class Testtwo:
    @pytest.mark.skip
    @pytest.mark.smoke
    def test_SignupPage_createShopifyID(self,testdata):
        self.driver.find_element(By.ID, 'account_first_name').send_keys(testdata[0])
        self.driver.find_element(By.ID, 'account_last_name').send_keys(testdata[1])
        self.driver.find_element(By.ID, 'account_email').send_keys(testdata[2])
        sleep(3)
        self.driver.find_element(By.ID, 'account_password').send_keys(testdata[3])
        self.driver.find_element(By.ID, 'password-confirmation').send_keys(testdata[4])
        ShopifyID_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        create_ShopifyID_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        assert create_ShopifyID_button.is_enabled()


    def test_SignUpPage_check_the_Login_functionality_from_signup_page(self):
        signuppage=SignUpPage(self.driver)
        signuppage.LogIn()
        title=self.driver.title
        print(title)
        assert "Log in - Shopify" in title
        print()