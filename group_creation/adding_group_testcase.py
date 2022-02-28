# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_adding_group_testcase(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(group_name="First group", group_header="1 group", group_footer="The first added group"))
    app.logout()

def test_adding_empty_group_testcase(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(group_name="", group_header="", group_footer=""))
    app.logout()








