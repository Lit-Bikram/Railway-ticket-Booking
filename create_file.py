import csv
import os

# details = [
#     [
#         {'first_name': 'Arijit', 'last_name': 'Singh', 'age': 50, 'gender': 'male'},
#         {'first_name': 'Shreya', 'last_name': 'Ghoshal','age': 40, 'gender': 'female'},
#         {'first_name': 'Sonu', 'last_name': 'Nigam', 'age': 55, 'gender': 'male'},
#         {'first_name': 'Lata', 'last_name': 'Mangeshkar','age': 70, 'gender': 'female'}
#     ],
#     [
#         {'first_name': 'John', 'last_name': 'Doe', 'age': 25, 'gender': 'male'}
#     ],
#     [
#         {'first_name': 'Alice', 'last_name': 'Smith', 'age': 30, 'gender': 'female'},
#         {'first_name': 'Bob', 'last_name': 'Johnson', 'age': 35, 'gender': 'male'}
#     ],
#     [
#         {'first_name': 'Emma', 'last_name': 'Brown', 'age': 28, 'gender': 'female'},
#     ],
#     [
#         {'first_name': 'Daniel', 'last_name': 'Williams', 'age': 40, 'gender': 'male'},
#         {'first_name': 'Grace', 'last_name': 'Miller', 'age': 62, 'gender': 'female'}
#     ],
#     [
#         {'first_name': 'Ryan', 'last_name': 'Davis', 'age': 32, 'gender': 'male'},
#         {'first_name': 'Sophia', 'last_name': 'Wilson','age': 29, 'gender': 'female'},
#         {'first_name': 'Michael', 'last_name': 'Jones', 'age': 45, 'gender': 'male'}
#     ],
#     [
#         {'first_name': 'Mukesh', 'last_name': 'Ambani', 'age': 65, 'gender': 'male'}
#     ],
#     [
#         {'first_name': 'Ethan', 'last_name': 'Martinez', 'age': 38, 'gender': 'male'},
#         {'first_name': 'Ava', 'last_name': 'Lee', 'age': 26, 'gender': 'female'},
#         {'first_name': 'William', 'last_name': 'Taylor', 'age': 33, 'gender': 'male'}
#     ],
#     [
#         {'first_name': 'Mia', 'last_name': 'Johnson', 'age': 31, 'gender': 'female'},
#         {'first_name': 'James', 'last_name': 'Clark', 'age': 29, 'gender': 'male'},
#         {'first_name': 'Noah', 'last_name': 'Ramirez', 'age': 41, 'gender': 'male'},
#         {'first_name': 'Liam', 'last_name': 'Perez', 'age': 67, 'gender': 'male'}
#     ],
#     [
#         {'first_name': 'Emily', 'last_name': 'Anderson','age': 23, 'gender': 'female'},
#         {'first_name': 'Abigail', 'last_name': 'Hill','age': 28, 'gender': 'female'},
#         {'first_name': 'Isabella', 'last_name': 'Baker','age': 30, 'gender': 'female'},
#         {'first_name': 'Logan', 'last_name': 'Garcia', 'age': 64, 'gender': 'male'},
#         {'first_name': 'Olivia', 'last_name': 'Moore', 'age': 27, 'gender': 'female'}
#     ]
# ]

def updateCsvFile(details):
    
    with open('data\passengers.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        row = []
        for item in details:
            f_name = item["first_name"]
            row.append(f_name)
            
            l_name = item["last_name"]
            row.append(l_name)
            
            age = item["age"]
            row.append(age)
            
            gender = item["gender"]
            row.append(gender)
            
        writer.writerow(row)
    return

def fileExist():
    if os.path.exists("data\passengers.csv"):
        return True
    else:
        with open('data\passengers.csv', 'a', newline='') as file:
            fieldnames = []
            writer = csv.writer(file)
            
            for i in range(6):
                fieldnames.append("first_name {}".format(i+1))
                fieldnames.append("last_name {}".format(i+1))
                fieldnames.append("age {}".format(i+1))
                fieldnames.append("gender {}".format(i+1))
            writer.writerow(fieldnames)
        return True

def appendData(details):
    if fileExist():
        updateCsvFile(details)
        
def readdata():
    with open('data/passengers.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            temp = []
            for i in range(int(len(row)/4)):
                record = {}
                record["first_name"] = row[i]
                record["last_name"] = row[i + 1]
                record["age"] = row[i + 2]
                record["gender"] = row[i + 3]
                temp.append(record)
                
    return

def waitingList(item):
    with open("data/waitinglist.csv", 'a', newline='') as file:
        # Check if the file is empty (no headers)
        file.seek(0, 2)
        is_empty = file.tell() == 0

        fieldnames = ['first_name', 'last_name', 'age', 'gender']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # If the file is empty, write the headers
        if is_empty:
            writer.writeheader()

        # Write the new data
        writer.writerow(item)
    return
