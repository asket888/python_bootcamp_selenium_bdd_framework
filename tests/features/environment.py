from pages.authentication_page import AuthenticationPage
from pages.header_section import HeaderSection
from utils.capabilities_util import get_driver


def before_all(context):
    # setup global variables
    setup = context.config.userdata
    context.driver = get_driver(browser=setup["browser"])
    # setup page_objects
    context.header_section = HeaderSection(context=context)
    context.authentication_page = AuthenticationPage(context=context)
    # open application under test
    context.authentication_page.go_to_url(url="http://automationpractice.com/index.php")


def after_all(context):
    context.authentication_page.quite()
