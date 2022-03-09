from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, Contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.contact_data(Contact)
        wd.find_element_by_name("submit").click()

    def delete(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_contact(self, Contact):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.contact_data(Contact)
        wd.find_element_by_name("update").click()

    def contact_data(self, Contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contact.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Contact.company_title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contact.company_name)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Contact.primary_address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contact.home_phone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contact.mobile_phone)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contact.work_phone)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(Contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contact.email1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(Contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(Contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Contact.homepage)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(Contact.birth_Day)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(Contact.birth_Month)
        wd.find_element_by_name("byear").send_keys(Contact.birth_Year)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(Contact.ann_Day)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(Contact.ann_Month)
        wd.find_element_by_name("ayear").send_keys(Contact.ann_Year)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Contact.secondary_address)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Contact.secondary_phone)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Contact.notes)

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()