from models.сontact import Contact
from models.group import Group
from fixtures.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_del_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    db.remove_all_contacts_from_all_groups()
    db.add_random_contact_to_random_group(contact.id, group.id)
    app.contact.del_from_group_by_id(contact.id, group.id)
    assert orm.get_contacts_in_group(Group(id=group.id)) == []