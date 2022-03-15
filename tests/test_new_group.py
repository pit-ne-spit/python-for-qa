# -*- coding: utf-8 -*-
from models.group import Group

def test_new_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="First group", group_header="1 group", group_footer="The first added group")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_new_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="", group_header="", group_footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)







