# E22.Classes and Objects in Python.
class Person:
    name = "Himanshu"
    occupation = "Software Engineer."
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a = Person()
b = Person()
c = Person()
a.name = "Divya"
a.occupation = "Data Scientist."
b.name = "Prashant"
b.occupation = "Data Analyst."
# print(a.name, a.occupation).
a.info()
b.info()
c.info()