from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(browser: str):
    if browser.upper() == "CH":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser.upper() == "CH_HL":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-setuid-sandbox")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    else:
        raise KeyError(
            f"Unexpected browser '{browser.upper()}'." f"Check your behave.ini file for available variables")
    driver.set_window_size(width=1200, height=800)
    return driver
