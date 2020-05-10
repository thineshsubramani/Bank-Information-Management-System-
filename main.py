import csv
import datetime

def load_data():
    # Load Data into Volatile memory so easy to work on the file.
    get_temp_data = []
    with open("User_data.csv", "r", newline='') as file:
        read = csv.DictReader(file)
        for row in read:
            print(row)
    #Loaded Into List
    return get_temp_data

def update_date():
    pass
def delete_data():
    pass
def search_data():
    pass
def view_data():
    pass
def create_data():
    temp_data = {}
    unique = input("Enter Card Number : ")
    name = input("Enter Name : ")
    age = input("Enter Age : ")
    id = input("Enter NRIC : ")
    cash = float(input("Enter Deposit RM : "))
    temp_data["Card Number"] =unique
    temp_data["Name"] = name
    temp_data["Age"] = age
    temp_data["NRIC"] =id
    temp_data["Amount (RM)"] = cash
    x = datetime.datetime.now()
    temp_data["Date"] = x.strftime("%d-%m-%Y")
    print("Saving Data...")
    with open("User_data.csv", "a",newline='') as file:
        csv_writer = csv.DictWriter(file,fieldnames=["Card Number","Name","Age","NRIC","Amount (RM)","Date"])
        csv_writer.writerow(temp_data)

    # Once new file



print("Welcome to Main menu \n 1: Enter Data \n Update Data \n Delete Data \n View Data \n Please Choose the option :")

opt = input();
if opt == "1":
    create_data()
else:
    load_data()


