from random import randrange
import re

def test_contact_data(app):
    contact_from_homepage = app.contact.get_contact_list()
    index = randrange(len(contact_from_homepage))
    selected_contact_on_home_page = contact_from_homepage[index]
    selected_contact_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert selected_contact_on_home_page.id == selected_contact_edit_page.id
    assert selected_contact_on_home_page.firstname == selected_contact_edit_page.firstname
    assert selected_contact_on_home_page.lastname == selected_contact_edit_page.lastname
    assert selected_contact_on_home_page.address == selected_contact_edit_page.address
    assert selected_contact_on_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(selected_contact_edit_page)
    assert selected_contact_on_home_page.all_emails == merge_emails_like_on_homepage(selected_contact_edit_page)


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