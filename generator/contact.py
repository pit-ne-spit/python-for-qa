from models.сontact import Contact
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, "w") as out:
    out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))