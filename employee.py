import json
class Employee:
    def __init__(self,Name, DOB, Height, City, State):
        self.Name =Name
        self.DOB =DOB
        self.Height =Height
        self.City =City
        self.State =State
    def __str__(self):
         return f"Name: {self.Name} , DOB : {self.DOB}, Height: {self.Height} , City : {self.City} , State: {self.State} "

with open(r"D:\test file1\_1_datatype\Assignment_file.py\employee.json") as file:
        data =json.load(file)
        employee_data = data.get('employee')
employee_list = []

for item in employee_data:
        employee = Employee(item.get('Name'), item.get('DOB'), item.get('Height'), item.get('City'), item.get('State'))
        employee_list.append(employee)
for employee in employee_list:
    print(employee)       


        