import csv

def isValidName(name):
    return name.isalpha()

def isValidPhone(phone):
    return phone.isdigit() and len(phone) == 11

def isValidSex(sex):
    return sex.lower() in ('male', 'female', 'other')

def addEntry(name, phone, sex, date):
    if not isValidName(name):
        print("Invalid name. Please enter alphabethic characters only.")
    elif not isValidPhone(phone):
        print("Invalid phone number. Please enter a valid phone number.")
    elif not isValidSex(sex):
        print("Invalid sex. Please enter with only the given option.")
    elif name and phone and sex and date:
        with open ('contactTracing.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, sex, date])
        print("Entry added successfully!")
        
    else:
        print("Please fill in all fields. Thank you!")
        
def searchEntry(name):
    if name:
        with open('contactTracing.csv', 'r') as file:
            reader = csv.reader(file)
            foundEntries = [entry for entry in reader if entry[0] == name]
            
            if foundEntries:
                print("Matching entries:")
                for entry in foundEntries:
                    print(
                        f"Name: {entry[0]}, Phone: {entry[1]}, Sex: = {entry[2]}, Date: {entry[3]}")
            
            else:
                print("No Matching Entry Found.")
    else:
        print("Please Enter a name to search.")
         