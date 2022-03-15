from models.сontact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Petr", middlename="V.", lastname="Arapov", nickname="pit_ne_spit", company_name="any",company_title="title of what?",
                                             primary_address="Sadovaya st., 555", home_phone="789456123", mobile_phone="+98456321", work_phone="85295217563", fax="789632147",
                                             email1="email1@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru", birth_Day="3", birth_Month="June", birth_Year="1988",
                                             ann_Day="2", ann_Month="February", ann_Year="2000", homepage="hmpg.ru",secondary_address="Beregovaya st., 585",
                                             secondary_phone="too much fields", notes="no notes"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

