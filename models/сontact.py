from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, email1=None, email2=None, email3=None, home_phone=None, mobile_phone=None,
                 work_phone=None, fax=None, birth_Day=None, birth_Month=None, birth_Year=None, ann_Day=None, ann_Month=None, ann_Year=None, secondary_address=None, secondary_phone=None, notes=None, company_title=None,
                 company_name=None, homepage=None, primary_address=None, id=None, all_phones_from_homepage=None, address=None, all_emails=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.birth_Day = birth_Day
        self.birth_Month = birth_Month
        self.birth_Year = birth_Year
        self.ann_Day = ann_Day
        self.ann_Month = ann_Month
        self.ann_Year = ann_Year
        self.secondary_address = secondary_address
        self.secondary_phone = secondary_phone
        self.notes = notes
        self.company_title = company_title
        self.company_name = company_name
        self.homepage = homepage
        self.primary_address = primary_address
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.address = address
        self.all_emails = all_emails


    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.firstname, self.lastname, self.id, self.address,  self.home_phone,
                                                  self.work_phone, self.mobile_phone, self.email1, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname and self.address == other.address, self.home_phone == other.home_phone, \
               self.work_phone == other.work_phone, self.mobile_phone == other.mobile_phone, self.email1 == other.email1, \
               self.email2 == other.email2, self.email3 == other.email3

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize