# E33.Class Methods as Alternative Constructors in Python.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
e1 = Employee("Himanshu", 12000)
print(e1.name)
print(e1.salary)
string = "Divya-12000"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))
person = Person.from_string("Prashant, 30")
print(person.name, person.age)