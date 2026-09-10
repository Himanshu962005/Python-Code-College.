# E41.Multiple Inheritance in Python.
class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The Name is {self.name}")
class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"The Dance is {self.dance}")
class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name
o = DancerEmployee("Kathak", "Divya")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())