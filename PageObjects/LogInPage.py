from selenium.webdriver.common.by import By

from PageObjects.SignUpPage import SignUpPage


class LogInPage:
    def __init__(self,driver):
        self.driver=driver

    Next=(By.NAME,'commit')
    GetStarted=(By.LINK_TEXT,'Get started')
    HeaderContent=(By.XPATH,'//div[@class="main-card-section"]/h1')

    def getNextbutton(self):
        return self.driver.find_element(*LogInPage.Next)

    def getStarted(self):
        getStartedButton=self.driver.find_element(*LogInPage.GetStarted)
        getStartedButton.click()
        signuppage=SignUpPage(self.driver)
        return signuppage
    def getHeaderContent(self):
        content=self.driver.find_element(*LogInPage.HeaderContent)
        return content.text
