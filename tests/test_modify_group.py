from models.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(group_name="New group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(group_header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)