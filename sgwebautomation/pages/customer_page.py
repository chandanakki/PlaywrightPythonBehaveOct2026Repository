from playwright.sync_api import Page

class CustomerPage:
    def __init__(self, page:Page):
        self.page=page
        self.lnk_customers_menu_field=page.locator("//a[normalize-space()='Customers']")
        self.btn_add_customers_button=page.locator("//a[normalize-space()='Add Customer']")
        self.txt_customername_textfield=page.locator("//input[@placeholder='Enter Customer Name']")
        self.txt_customeremail_textfield=page.locator("//input[@placeholder='Enter EmailId']")
        self.txt_customerlocation_textfield=page.locator("//input[@placeholder='Enter Location']")
        self.txt_customerdescription_textfield=page.locator("//input[@placeholder='Enter Description']")
        self.btn_customer_save_buttonfield=page.locator("//button[normalize-space()='Save']")


    def click_customers_menu(self):
       self.lnk_customers_menu_field.click() 

    def click_add_customers_button(self):
        self.btn_add_customers_button.click()

    def set_customer_name_field(self,customername):
        self.txt_customername_textfield.fill(customername)

    def set_customer_emailid_field(self,emailid):
        self.txt_customeremail_textfield.fill(emailid)

    def set_customer_location_field(self,location):
        self.txt_customerlocation_textfield.fill(location)

    def set_customer_description_field(self,description):
        self.txt_customerdescription_textfield.fill(description)

    def click_customer_save_button(self):
        self.btn_customer_save_buttonfield.click()
