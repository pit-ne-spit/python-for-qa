import time

def test_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete()
    app.session.logout()