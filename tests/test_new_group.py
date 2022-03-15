# -*- coding: utf-8 -*-
from models.group import Group

def test_new_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(group_name="First group", group_header="1 groupn", group_footer="The first added group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_new_empty_group(app):
    app.group.create(Group(group_name="", group_header="", group_footer=""))








