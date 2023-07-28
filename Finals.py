import csv
import tkinter as tk
from tkinter import messagebox


def isValidName(name):
    return name.isalpha()

def isValidPhone(phone):
    return phone.isdigit() and len(phone) == 11

def isValidSex(sex):
    return sex.lower() in ('male', 'female', 'other')

def addEntry():
    name = entry_name.get()
    phone = entry_phone.get()
    sex = entry_sex.get()
    date = entry_date.get()
    
    if not isValidName(name):
        messagebox.showerror(
        "Error", "Invalid name. Please enter alphabethic characters only.")
    elif not isValidPhone(phone):
        messagebox.showerror(
            "Error", "Invalid phone number. Please enter a valid phone number.")
    elif not isValidSex(sex):
        messagebox.showerror(
            "Error", "Invalid sex. Please enter with only the given option.")
    elif name and phone and sex and date:
        with open ('contactTracing.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, sex, date])
        messagebox.showinfo("Entry added successfully!")
        
    else:
        messagebox.showerror("Please fill in all fields. Thank you!")
        
def searchEntry():
    name = entry_name.get()
    if name:
        with open('contactTracing.csv', 'r') as file:
            reader = csv.reader(file)
            foundEntries = [entry for entry in reader if entry[0] == name]
            
            if foundEntries:
                result_text.set("\n".join(
                    [f"Name: {entry[0]}, Phone: {entry[1]}, Sex: {entry[2]}, Date: {entry[3]}" for entry in foundEntries]))
            
            else:
                result_text.set("No Matching Entry Found.")
    else:
        result_text.set("Please Enter a name to search.")
        

root = tk.Tk()
root.title("COVID Contact Tracing App")

label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

label_sex = tk.Label(root, text="Sex (male/female/other):")
label_sex.grid(row=2, column=0)
entry_sex = tk.Entry(root)
entry_sex.grid(row=2, column=1)

label_date = tk.Label(root, text="Date:")
label_date.grid(row=3, column=0)
entry_date = tk.Entry(root)
entry_date.grid(row=3, column=1)

btn_add = tk.Button(root, text="Add Entry", command=addEntry)
btn_add.grid(row=4, column=0, columnspan=2)

btn_search = tk.Button(root, text="Search Entry", command=searchEntry)
btn_search.grid(row=5, column=0, columnspan=2)

result_text = tk.StringVar()
label_result = tk.Label(root, textvariable=result_text)
label_result.grid(row=6, column=0, columnspan=2)

root.mainloop()
