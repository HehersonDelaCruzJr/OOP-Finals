import csv

def isValidName(name):
    return name.isalpha()

def isValidPhone(phone):
    return phone.isdigit() and len(phone) == 11

def isValidSex(sex):
    return sex.lower() in ('male', 'female', 'other')