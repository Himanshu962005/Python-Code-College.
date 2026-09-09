# E34.Dir, __Dict__ and Help Method in Python.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
p = Person("Himanshu", 30)
print(p.__dict__)
print(help(Person))