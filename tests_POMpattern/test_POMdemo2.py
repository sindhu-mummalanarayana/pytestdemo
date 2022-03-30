import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.SignUpPage import SignUpPage


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("testdata")
class Testtwo:

    @pytest.mark.smoke
    def test_SignupPage_createShopifyID(self,testdata):
        self.driver.find_element(By.ID, 'account_first_name').send_keys(testdata[0])
        self.driver.find_element(By.ID, 'account_last_name').send_keys(testdata[1])

        ShopifyID_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        create_ShopifyID_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        assert create_ShopifyID_button.is_enabled()

)