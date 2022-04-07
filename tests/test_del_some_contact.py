from models.сontact import Contact
from random import randrange
import random


def test_del_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Petr", middlename="V.", lastname="Arapov", nickname="pit_ne_spit", company_name="any",company_title="title of what?",
                                             primary_address="Sadovaya st., 555", home_phone="789456123", mobile_phone="+98456321", work_phone="85295217563", fax="789632147",
                                             email1="email1@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru", birth_Day="3", birth_Month="June", birth_Year="1988",
                                             ann_Day="2", ann_Month="February", ann_Year="2000", homepage="hmpg.ru",secondary_address="Beregovaya st., 585",
                                             secondary_phone="too much fields", notes="no notes"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)

