# E32.Class Methods in Python.
class Employee:
    company = "Google"
    def show(self):
        print(f"The Name is {self.name} and Company is {self.company}.")
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany
e1 = Employee()
e1.name = "Himanshu"
e1.show()
e1.changeCompany("YouTube")
e1.show()
print(Employee.company)