# -*- coding: utf-8 -*-
from models.сontact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits(prefix, maxlen):
    return prefix + "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])

test_data = [
    Contact(firstname=random_string("A", 10), middlename=random_string("B", 10), lastname=random_string("V", 10),
            nickname=random_string("FG", 10), company_name=random_string("weqc", 10), company_title=random_string("title", 10),
            primary_address=random_string("", 10), home_phone=random_digits("8", 10),
            mobile_phone=random_digits("7", 10), work_phone=random_digits("8", 10), fax=random_digits("8", 10),
            email1=random_string("", 8), email2=random_string("", 8), email3=random_string("", 8), birth_Day="3",
            birth_Month="June", birth_Year="1988", ann_Day="2", ann_Month="February", ann_Year="2000", homepage="hmpg.ru",
            secondary_address=random_string("Secar", 15), secondary_phone=random_digits("+7", 10), notes="no notes")
    for i in range(2)
]

@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

