from playwright.sync_api import Page

class HomePage:
    def __init__(self,page:Page):
        self.page=page
        self.lnk_logout_linkfield=page.locator("//button[normalize-space()='Logout']")

    def click_on_logout_link(self):
        self.lnk_logout_linkfield.click()