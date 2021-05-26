from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderSection(BasePage):

    __HEADER_LOGIN_BUTTON = (By.XPATH, "//a[@class='login']")
    __HEADER_LOGOUT_BUTTON = (By.XPATH, "//a[@class='logout']")
    __HEADER_NICKNAME_TEXT = (By.XPATH, "//a[@title='View my customer account']")

    def click_login_button(self):
        self.click(self.__HEADER_LOGIN_BUTTON)

    def check_if_nickname_is_presented(self):
        self.get_element(self.__HEADER_NICKNAME_TEXT)
        return True

    def click_logout_button(self,):
        self.click(self.__HEADER_LOGOUT_BUTTON)

    def check_if_nickname_is_not_presented(self):
        if_nickname_visible = True
        try:
            self.get_element(self.__HEADER_NICKNAME_TEXT)
        except TimeoutException:
            if_nickname_visible = False
        return if_nickname_visible
