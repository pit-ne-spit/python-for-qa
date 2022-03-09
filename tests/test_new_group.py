# -*- coding: utf-8 -*-
from models.group import Group

def test_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="First group", group_header="1 groupn", group_footer="The first added group"))
    app.session.logout()

def test_new_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="", group_header="", group_footer=""))
    app.session.logout()








