from curses.ascii import isdigit


class validate_LL:
    def __init__(self):
        pass

    def validate_email(self, email):
        """This is the validation for email"""
        if "@" in email and "." in email:
            return True
        return False

    def validate_phone_number(self, phone_number):
        """This is the validation for phone number"""
        if len(phone_number) == 7 and isdigit(phone_number):
            return True
        return False

    def validate_name(self, name):
        """This is the validation for name"""
        if name.isalpha():
            return True
        return False

    def validate_id(self, id):
        """This is the validation for id"""
        if (isdigit(id) and len(id) == 10) or (len(id) == 11 and id[6] == "-" and isdigit(id.replace("-", ""))):
            return True
        return False