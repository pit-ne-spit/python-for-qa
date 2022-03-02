# -*- coding: utf-8 -*-
import pytest
from fixtures.application import Application
from models.сontact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_new_contact(app):
    app.session.login(username="admin", password="secret")

    app.contact.create(Contact(firstname="Petr", middlename="V.", lastname="Arapov", nickname="pit_ne_spit", company_name="any",company_title="title of what?",
                                             primary_address="Sadovaya st., 555", home_phone="789456123", mobile_phone="+98456321", work_phone="85295217563", fax="789632147",
                                             email1="email1@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru", birth_Day="3", birth_Month="June", birth_Year="1988",
                                             ann_Day="2", ann_Month="February", ann_Year="2000", homepage="hmpg.ru",secondary_address="Beregovaya st., 585",
                                             secondary_phone="too much fields", notes="no notes"))

    app.session.logout()
