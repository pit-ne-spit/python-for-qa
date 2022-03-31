from models.сontact import Contact
import random
import string

constant = [
    Contact(firstname="Ivan", middlename="I.", lastname="Ivanov", nickname="Uncle_Ivan", company_name="Ivan_pickles_ltd",
            company_title="title", primary_address="Pushkina, 10", home_phone="8", mobile_phone="7",
            work_phone="8", fax="8", email1="11@11.ru", email2="22@22.ru", email3="33@33.ru", birth_Day="3",
            birth_Month="June", birth_Year="1988", ann_Day="2", ann_Month="February", ann_Year="2000", homepage="hmpg.ru",
            secondary_address="Secar", secondary_phone="+7", notes="no notes")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
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
