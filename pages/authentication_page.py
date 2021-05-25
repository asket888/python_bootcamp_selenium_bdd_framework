from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AuthenticationPage(BasePage):

    __AUTHENTICATION_EMAIL_FIELD = (By.ID, "email")
    __AUTHENTICATION_PASSWORD_FIELD = (By.ID, "passwd")
    __AUTHENTICATION_SUBMIT_BUTTON = (By.ID, "SubmitLogin")

    def login_to_application(self):
        self.fill(by_locator=self.__AUTHENTICATION_EMAIL_FIELD, value="test_bootcamp@gmail.com")
        self.fill(by_locator=self.__AUTHENTICATION_PASSWORD_FIELD, value="123456")
        self.click(by_locator=self.__AUTHENTICATION_SUBMIT_BUTTON)
