from models.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test"))
    app.group.modify_first_group(Group(group_name="New group"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(group_header="New header"))
