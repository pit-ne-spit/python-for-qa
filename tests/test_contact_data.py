from random import randrange
import re
from models.сontact import Contact

def test_contact_data(app, db):
    contacts_from_homepage = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()

    assert sorted(contacts_from_homepage, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)
    pass
    # assert selected_contact_on_home_page.firstname == selected_contact_edit_page.firstname
    # assert selected_contact_on_home_page.lastname == selected_contact_edit_page.lastname
    # assert selected_contact_on_home_page.address == selected_contact_edit_page.address
    # assert selected_contact_on_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(selected_contact_edit_page)
    # assert selected_contact_on_home_page.all_emails == merge_emails_like_on_homepage(selected_contact_edit_page)


# def clear(s):
#     return re.sub("[()-]", "", s)
#
#
# def merge_phones_like_on_homepage(contact):
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x: clear(x),
#                                 filter(lambda x: x is not None,
#                                        [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]))))
#
#
# def merge_emails_like_on_homepage(contact):
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x: clear(x),
#                                 filter(lambda x: x is not None,
#                                        [contact.email1, contact.email2, contact.email3]))))