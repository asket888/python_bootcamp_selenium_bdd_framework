from behave import step
from hamcrest import assert_that, is_


@step("I click [Login] button on the header of the page")
def step_impl(context):
    context.header_section.click_login_button()


@step("nickname is presented on the header of the page")
def step_impl(context):
    if_nickname_visible = context.header_section.check_if_nickname_is_presented()
    assert_that(if_nickname_visible, is_(True))


@step("I click [Logout] button on the header of the page")
def step_impl(context):
    context.header_section.click_logout_button()


@step("nickname is not presented on the header of the page")
def step_impl(context):
    if_nickname_visible = context.header_section.check_if_nickname_is_not_presented()
    assert_that(if_nickname_visible, is_(False))
