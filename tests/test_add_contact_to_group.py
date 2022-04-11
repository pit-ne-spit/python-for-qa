from models.сontact import Contact
from random import randrange
from models.group import Group
import random


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="Petr", middlename="V.", lastname="Arapov", nickname="pit_ne_spit", company_name="any",
                    company_title="title of what?",
                    primary_address="Sadovaya st., 555", home_phone="789456123", mobile_phone="+98456321",
                    work_phone="85295217563", fax="789632147",
                    email1="email1@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru", birth_Day="3",
                    birth_Month="June", birth_Year="1988",
                    ann_Day="2", ann_Month="February", ann_Year="2000", homepage="hmpg.ru",
                    secondary_address="Beregovaya st., 585",
                    secondary_phone="+7848813232", notes="no notes"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    app.contact.add_contact_to_group_by_id(contact.id, group.id)



