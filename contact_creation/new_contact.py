# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

from personal_information import PersonalInformation

class new_contact_creation_test(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path='./chromedriver')
        self.wd.implicitly_wait(30)
    
    def test_new_contact(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.open_add_page(wd)

        # first, last, middle names & nickname
        self.personal_infomation(wd, PersonalInformation(firstname="Petr", middlename="V.", lastname="Arapov", nickname="pit_ne_spit"))

        self.work_infomation(wd, company_name="any", company_title="title of what?")
        self.address(wd, primary_address="Sadovaya st., 555")
        self.phones_and_fax(wd, home_phone="789456123", mobile_phone="+98456321", work_phone="85295217563", fax="789632147")
        self.emails(wd, email1="email1@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru")
        self.web_address(wd, homepage="hmpg.ru")
        self.date_of_birth(wd, birthDay="3", birthMonth="June", birthYear="1988")
        self.anniversary_date(wd, annDay="2", annMonth="February", annYear="2000")
        # second address, home & notes
        self.secondary_information(wd, secondary_address="Beregovaya st., 585", secondary_phone="to much fields", notes="no notes")
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def secondary_information(self, wd, secondary_address, secondary_phone, notes):
        wd.find_element_by_name("address2").send_keys(secondary_address)
        wd.find_element_by_name("phone2").send_keys(secondary_phone)
        wd.find_element_by_name("notes").send_keys(notes)

    def anniversary_date(self, wd, annDay, annMonth, annYear):
        Select(wd.find_element_by_name("aday")).select_by_visible_text(annDay)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(annMonth)
        wd.find_element_by_name("ayear").send_keys(annYear)

    def date_of_birth(self, wd, birthDay, birthMonth, birthYear):
        Select(wd.find_element_by_name("bday")).select_by_visible_text(birthDay)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(birthMonth)
        wd.find_element_by_name("byear").send_keys(birthYear)

    def web_address(self, wd, homepage):
        wd.find_element_by_name("homepage").send_keys(homepage)

    def emails(self, wd, email1, email2, email3):
        wd.find_element_by_name("email").send_keys(email1)
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").send_keys(email3)

    def phones_and_fax(self, wd, home_phone, mobile_phone, work_phone, fax):
        wd.find_element_by_name("home").send_keys(home_phone)
        wd.find_element_by_name("mobile").send_keys(mobile_phone)
        wd.find_element_by_name("work").send_keys(work_phone)
        wd.find_element_by_name("fax").send_keys(fax)

    def address(self, wd, primary_address):
        wd.find_element_by_name("address").send_keys(primary_address)

    def work_infomation(self, wd, company_name, company_title):
        wd.find_element_by_name("title").send_keys(company_title)
        wd.find_element_by_name("company").send_keys(company_name)

    def personal_infomation(self, wd, PersonalInformation):
        wd.find_element_by_name("firstname").send_keys(PersonalInformation.firstname)
        wd.find_element_by_name("middlename").send_keys(PersonalInformation.middlename)
        wd.find_element_by_name("lastname").send_keys(PersonalInformation.lastname)
        wd.find_element_by_name("nickname").send_keys(PersonalInformation.nickname)

    def open_add_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
    

