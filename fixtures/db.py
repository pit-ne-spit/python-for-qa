import pymysql.cursors
from models.group import Group
from models.сontact import Contact

class Dbfixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), group_name=name, group_header=header, group_footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 "
                           "from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email1, email2, email3, home, mobile, work, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,  home_phone=home,
                                    mobile_phone=mobile, work_phone=work, secondary_phone=phone2, email1=email1, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def remove_all_contacts_from_random_group(self, group_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("delete from address_in_groups where group_id = {group_id}")
        finally:
            cursor.close()

    def remove_all_contacts_from_all_groups(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("delete from address_in_groups")
        finally:
            cursor.close()

    def add_random_contact_to_random_group(self, contact_id, group_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"INSERT INTO `address_in_groups` (`domain_id`, `id`, `group_id`, `created`, `modified`, `deprecated`) VALUES "
                f"('0', '{contact_id}', '{group_id}', '2022-04-10 00:00:00', '2022-04-10 00:00:00', '0000-00-00 00:00:00')")
        finally:
            cursor.close()

    def get_contact_id_in_group_list(self, contact_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from address_in_groups where id = {contact_id}")
            for row in cursor:
                (id) = row
                list.append(Contact(id=str(id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()