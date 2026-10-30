from playwright.sync_api import expect
from behave import when, then
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.customer_page import CustomerPage

@when(u'I Launch browser and navigate URL')
def i_launch_browser_and_navigate_url(context):
    context.page.goto("https://sgtestinginstituteapp.onrender.com/")
    # Create Page Objects
    context.login=LoginPage(context.page)
    context.home=HomePage(context.page)
    context.customer=CustomerPage(context.page)

@then(u'I find the login page')
def i_find_the_login_page(context):
    expect(context.page).to_have_title("S G Software Testing Institute")
    expect(context.page).to_have_url("https://sgtestinginstituteapp.onrender.com/login")
    expect(context.page.locator("//h2[normalize-space()='Login']")).to_have_text("Login")

@when(u'I enter username in username text field')
def i_enter_username_in_username_textfield(context):
    context.login.set_username_textfield("pgudi")


@when(u'I enter password in password text field')
def i_enter_password_in_password_textfield(context):
    context.login.set_password_textfield("pgudi")

@when(u'I click on signin button')
def i_click_on_signin_button(context):
    context.login.click_signin_buttonfield()


@then(u'I find the Home page')
def i_find_the_home_page(context):
    expect(context.page.locator("//h2[normalize-space()='S G Software Testing Institute']")).to_have_text("S G Software Testing Institute")

@when(u'I enter invalid username in username text field')
def i_enter_invalid_username(context):
    context.login.set_username_textfield("pgudi123")


@when(u'I enter invalid password in password text field')
def i_enter_invalid_password(context):
    context.login.set_password_textfield("pgudi123")

@then(u'I find the error message Invalid username or password')
def i_find_error_message_in_login_page(context):
    expect(context.page.locator("//p[normalize-space()='Invalid username or password']")).to_be_visible()

@when(u"I click on logout link")
def i_click_on_logout_link(context):
    context.home.click_on_logout_link()

@when(u"I enter {username} in username text field")
def i_enter_data_in_usernamefield(context, username):
    context.login.set_username_textfield(username)

@when(u"I enter {password} in password text field")
def i_enter_data_in_passwordfield(context, password):
    context.login.set_password_textfield(password)

@when(u'I click on customers menu')
def i_click_customers_menu(context):
    context.customer.click_customers_menu()


@then(u'I find list customers page')
def i_find_list_cistomer_page(context):
    expect(context.page.locator("//h4[normalize-space()='Display Customers']")).to_have_text("Display Customers")


@when(u'I click on add customer button')
def I_click_on_add_customers_button(context):
    context.customer.click_add_customers_button()


@then(u'I find add customer form')
def i_find_add_customer_form(context):
    expect(context.page.locator("//h3[normalize-space()='Add Customer']")).to_be_visible()


@when(u'I enter customername in customername text field')
def i_enter_customer_name(context):
    context.customer.set_customer_name_field("auto_service01")


@when(u'I enter emailid in emailid text field')
def i_enter_customer_emailid(context):
    context.customer.set_customer_emailid_field("auto_service01@sg.com")


@when(u'I enter location in location text field')
def i_enter_customer_location(context):
    context.customer.set_customer_location_field("Boston")


@when(u'I enter description in description text field')
def i_customer_description(context):
    context.customer.set_customer_description_field("Testing Purpose")


@when(u'I clcik on save button to create a customer')
def i_click_customer_save_button(context):
    context.customer.click_customer_save_button()


@then(u'I find newly created customer in list customers page')
def step_impl(context):
    expect(context.page.locator("//td[normalize-space()='auto_service01']")).to_be_visible()

@when(u"I click on delete button on newly created customer to delete customer")
def i_delete_newly_created_customer(context):
    context.page.on("dialog", lambda dialog:dialog.accept())
    context.page.locator("//td[text()='auto_service01']/following-sibling::td[4]/button[2]").click()

@then(u'I find that newly created customer is not available')
def deleted_customer_not_visiable(context):
    expect(context.page.locator("//td[normalize-space()='auto_service01']")).not_to_be_visible()