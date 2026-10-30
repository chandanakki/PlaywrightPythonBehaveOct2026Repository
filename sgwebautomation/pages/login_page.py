from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        self.page=page
        self.txt_username_textfield=page.locator("//input[@name='username']")
        self.txt_password_textfield=page.locator("//input[@name='password']")
        self.btn_signin_buttonfield=page.locator("//button[normalize-space()='Sign In']")

    def set_username_textfield(self, username):
        self.txt_username_textfield.fill(username)

    def set_password_textfield(self, password):
        self.txt_password_textfield.fill(password)

    def click_signin_buttonfield(self):
        self.btn_signin_buttonfield.click()