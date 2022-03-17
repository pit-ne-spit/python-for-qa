from models.group import Group

def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="New group")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(group_header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)