# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

from Contact import Contact

class NewContactCreationTest(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path='./chromedriver')
        self.wd.implicitly_wait(30)
    
    def test_new_contact(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.open_add_page(wd)

        # first, last, middle names & nickname
        self.contact_infomation(wd, Contact(firstname="Petr", middlename="V.", lastname="Arapov", nickname="pit_ne_spit", company_name="any",company_title="title of what?",
                                             primary_address="Sadovaya st., 555", home_phone="789456123", mobile_phone="+98456321", work_phone="85295217563", fax="789632147",
                                             email1="email1@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru", birthDay="3", birthMonth="June", birthYear="1988",
                                             annDay="2", annMonth="February", annYear="2000", homepage="hmpg.ru",secondary_address="Beregovaya st., 585",
                                             secondary_phone="too much fields", notes="no notes"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def contact_infomation(self, wd, Contact):
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
        Select(wd.find_element_by_name("bday")).select_by_visible_text(Contact.birthDay)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(Contact.birthMonth)
        wd.find_element_by_name("byear").send_keys(Contact.birthYear)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(Contact.annDay)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(Contact.annMonth)
        wd.find_element_by_name("ayear").send_keys(Contact.annYear)
        wd.find_element_by_name("address2").send_keys(Contact.secondary_address)
        wd.find_element_by_name("phone2").send_keys(Contact.secondary_phone)
        wd.find_element_by_name("notes").send_keys(Contact.notes)

    def open_add_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
    

