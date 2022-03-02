from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixtures.session import SessionHelper
from fixtures.group import GroupHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Chrome(executable_path='../chromedriver')
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def contact_infomation(self, Contact):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(Contact.firstname)
        wd.find_element_by_name("middlename").send_keys(Contact.middlename)
        wd.find_element_by_name("lastname").send_keys(Contact.lastname)
        wd.find_element_by_name("nickname").send_keys(Contact.nickname)
        wd.find_element_by_name("title").send_keys(Contact.company_title)
        wd.find_element_by_name("company").send_keys(Contact.company_name)
        wd.find_element_by_name("address").send_keys(Contact.primary_address)
        wd.find_element_by_name("home").send_keys(Contact.home_phone)
        wd.find_element_by_name("mobile").send_keys(Contact.mobile_phone)
        wd.find_element_by_name("work").send_keys(Contact.work_phone)
        wd.find_element_by_name("fax").send_keys(Contact.fax)
        wd.find_element_by_name("email").send_keys(Contact.email1)
        wd.find_element_by_name("email2").send_keys(Contact.email2)
        wd.find_element_by_name("email3").send_keys(Contact.email3)
        wd.find_element_by_name("homepage").send_keys(Contact.homepage)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(Contact.birth_Day)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(Contact.birth_Month)
        wd.find_element_by_name("byear").send_keys(Contact.birth_Year)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(Contact.ann_Day)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(Contact.ann_Month)
        wd.find_element_by_name("ayear").send_keys(Contact.ann_Year)
        wd.find_element_by_name("address2").send_keys(Contact.secondary_address)
        wd.find_element_by_name("phone2").send_keys(Contact.secondary_phone)
        wd.find_element_by_name("notes").send_keys(Contact.notes)


    def destroy(self):
        self.wd.quit()