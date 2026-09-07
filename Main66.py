# E23.Constructors in Python.
class Person:
    def __init__(self, name, occ):
        print("Hey, I am a Person.")
        self.name = name
        self.occ = occ
    def info(self):
        print(f"{self.name} is a {self.occ}.")
a = Person("Himanshu", "Engineer")
b = Person("Divya", "Developer")
a.info()
b.info()
# print(a.name).
# a.name = "Himanshu".
# a.occ = "Engineer".
# a.info().