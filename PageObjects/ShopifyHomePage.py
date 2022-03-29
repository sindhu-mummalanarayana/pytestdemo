from selenium.webdriver.common.by import By

from PageObjects.LogInPage import LogInPage


class ShopifyHomePage:
    def __init__(self,driver):
        self.driver=driver

    LogIn=(By.LINK_TEXT, 'Log in')
    EmailAddress_ForFreeTrail=(By.XPATH,'//input[contains(@id,"SignupEmail")]')

    def LogInButton(self):
        self.driver.find_element(*ShopifyHomePage.LogIn).click()
        loginpage=LogInPage(self.driver)
        return loginpage

    def getEmailAddress_ForFreeTrail(self):
        return self.driver.find_element(*ShopifyHomePage.EmailAddress_ForFreeTrail)