class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        if not wd.current_url.endswith("/edit.php"):
            wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.fname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.mname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lname)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage(wd)

    def return_to_homepage(self, wd):
        wd = self.app.wd
        if not(wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_homepage(wd)
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        self.return_to_homepage(wd)

    def edit_first_contact(self):
        wd = self.app.wd
        self.enter_editing_mode()
        # deleting some information
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        # confirm update
        wd.find_element_by_name("update").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_homepage(wd)
        self.enter_editing_mode()
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_homepage(wd)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.fname)
        self.change_field_value("middlename", contact.mname)
        self.change_field_value("lastname", contact.lname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def enter_editing_mode(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

