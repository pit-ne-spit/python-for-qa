from models.group import Group

def test_edit_first_group(app):
    app.group.edit_first_group(Group(group_name="Edited group name", group_header="Edited group header", group_footer="Text of text field edition"))
