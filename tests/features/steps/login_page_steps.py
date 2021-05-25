from behave import step


@step("I login to application on Login page")
def step_impl(context):
    context.authentication_page.login_to_application()
