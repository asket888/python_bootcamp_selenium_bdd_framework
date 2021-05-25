from behave.runner import Context
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, context: Context):
        self.driver = context.driver
        self.explicitly_wait = WebDriverWait(
            driver=self.driver,
            timeout=5
        )

    def go_to_url(self, url):
        self.driver.get(url)

    def get_element(self, by_locator):
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator),
                                   message=f"'{by_locator}' element doesn't appear on the page"
                                   )
        return self.driver.find_element(*by_locator)

    def click(self, by_locator):
        self.explicitly_wait.until(expected_conditions.element_to_be_clickable(by_locator),
                                   message=f"'{by_locator}' element doesn't appear on the page"
                                   )
        self.driver.find_element(*by_locator).click()

    def fill(self, by_locator, value):
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator),
                                   message=f"'{by_locator}' element doesn't appear on the page"
                                   )
        self.driver.find_element(*by_locator).send_keys(value)

    def quite(self):
        self.driver.quit()
