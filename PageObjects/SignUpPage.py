from selenium.webdriver.common.by import By

#from PageObjects.LogInPage import LogInPage


class SignUpPage:
    def __init__(self,driver):
        self.driver=driver

    login=(By.LINK_TEXT,"Log in")

    def LogIn(self):

        loginbutton=self.driver.find_element(*SignUpPage.login)
        loginbutton.click()



