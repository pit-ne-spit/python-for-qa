from random import randrange
import re
from models.сontact import Contact

def test_contact_data(app, db):
    contacts_list_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_list_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_list_ui) == len(contacts_list_db)
    for i in range(0, len(contacts_list_db)):
        contacts_from_homepage = contacts_list_ui[i]
        contacts_from_db = contacts_list_db[i]
        assert contacts_from_homepage.id == contacts_from_db.id
        assert contacts_from_homepage.firstname == contacts_from_db.firstname
        assert contacts_from_homepage.lastname == contacts_from_db.lastname
        assert contacts_from_homepage.address == contacts_from_db.address
        assert contacts_from_homepage.address == contacts_from_db.address
        assert contacts_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contacts_from_db)
        assert contacts_from_homepage.all_emails == merge_emails_like_on_homepage(contacts_from_db)


def clear(s):
    return re.sub("[()-]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))