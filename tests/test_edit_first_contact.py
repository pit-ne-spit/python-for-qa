from models.сontact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Petr", middlename="V.", lastname="Arapov", nickname="pit_ne_spit", company_name="any",company_title="title of what?",
                                             primary_address="Sadovaya st., 555", home_phone="789456123", mobile_phone="+98456321", work_phone="85295217563", fax="789632147",
                                             email1="email1@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru", birth_Day="3", birth_Month="June", birth_Year="1988",
                                             ann_Day="2", ann_Month="February", ann_Year="2000", homepage="hmpg.ru",secondary_address="Beregovaya st., 585",
                                             secondary_phone="too much fields", notes="no notes"))

    app.contact.edit_first_contact(Contact(firstname="Slam", middlename="Bi", lastname="Stoev", nickname="SBS", company_name="rock", company_title="n roll",
                                           primary_address="Vodnaya st., 555", home_phone="789456123", mobile_phone="+98456321", work_phone="85295217563", fax="789632147",
                                           email1="email1@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru", birth_Day="3", birth_Month="June", birth_Year="1988",
                                           ann_Day="2", ann_Month="February", ann_Year="2000", homepage="hmpg.ru", secondary_address="Beregovaya st., 585",
                                           secondary_phone="too much fields", notes="no notes"))
