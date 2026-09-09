# E30.Instance Variables V/S Class Variables in Python.
class Employee:
    companyName = "Google"
    noOfEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployees += 1
    def showDetails(self):
        print(f"The Name of the Employee is {self.name} and the Raise Amount in {self.noOfEmployees} Sized {self.companyName} is {self.raise_amount}.")
# Employee.showDetails(emp1).
emp1 = Employee("Himanshu")
emp1.raise_amount = 0.3
emp1.companyName = "Microsoft"
emp1.showDetails()
Employee.companyName = "Amazon"
print(Employee.companyName)
emp2 = Employee("Divya")
emp2.companyName = "Flipkart"
emp2.showDetails()