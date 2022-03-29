from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setupHome")
class Test0ne:
    def test_TC01_ShopifyHomepage_LoginButton(self):
        self.driver.find_element(By.LINK_TEXT, 'Log in').click()
        getstarted_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Get started")))

        self.driver.find_element(By.LINK_TEXT, "Get started").click()
        sleep(10)

