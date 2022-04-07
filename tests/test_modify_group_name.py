from models.group import Group
from random import randrange

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(group_name="New group")
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_modify_group_header(app):
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(group_header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)