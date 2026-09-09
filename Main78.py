# E35.Super keyword in Python.
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
Divya = Employee("Divya Pandey", "420")
Himanshu = Programmer("Himanshu", "962005", "Python")
print(Himanshu.name)
print(Himanshu.id)
print(Himanshu.lang)