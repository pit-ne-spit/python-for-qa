# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class new_contact_creation_test(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path='./chromedriver')
        self.wd.implicitly_wait(30)
    
    def test_new_contact(self):
        wd = self.wd
        self.login(wd)
        self.open_add_page(wd)

        # first, last, middle names & nickname
        self.personal_infomation(wd)

        self.work_infomation(wd)
        self.address(wd)
        self.phones_and_fax(wd)
        self.emails(wd)
        self.web_address(wd)
        self.date_of_birth(wd)
        self.anniversary_date(wd)
        # second address, home & notes
        self.secondary_information(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def secondary_information(self, wd):
        wd.find_element_by_name("address2").send_keys("Beregovaya, st., 585")
        wd.find_element_by_name("phone2").send_keys("to much fields")
        wd.find_element_by_name("notes").send_keys("no notes")

    def anniversary_date(self, wd):
        Select(wd.find_element_by_name("aday")).select_by_visible_text("2")
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("February")
        wd.find_element_by_name("ayear").send_keys("2000")

    def date_of_birth(self, wd):
        Select(wd.find_element_by_name("bday")).select_by_visible_text("3")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("June")
        wd.find_element_by_name("byear").send_keys("1988")

    def web_address(self, wd):
        wd.find_element_by_name("homepage").send_keys("hmpg.ru")

    def emails(self, wd):
        wd.find_element_by_name("email").send_keys("email1@mail.ru")
        wd.find_element_by_name("email2").send_keys("email2@mail.ru")
        wd.find_element_by_name("email3").send_keys("email3@mail.ru")

    def phones_and_fax(self, wd):
        wd.find_element_by_name("home").send_keys("789456123")
        wd.find_element_by_name("mobile").send_keys("+98456321")
        wd.find_element_by_name("work").send_keys("85295217563")
        wd.find_element_by_name("fax").send_keys("789632147")

    def address(self, wd):
        wd.find_element_by_name("address").send_keys("Sadovaya st., 555")

    def work_infomation(self, wd):
        wd.find_element_by_name("title").send_keys("title of what?")
        wd.find_element_by_name("company").send_keys("any")

    def personal_infomation(self, wd):
        wd.find_element_by_name("firstname").send_keys("Petr")
        wd.find_element_by_name("middlename").send_keys("V.")
        wd.find_element_by_name("lastname").send_keys("Arapov")
        wd.find_element_by_name("nickname").send_keys("pit_ne_spit")

    def open_add_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd):
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
    

