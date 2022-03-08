from models.group import Group

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(group_name="Edited group name", group_header="Edited group header", group_footer="Text of text field edition"))
    app.session.logout()
