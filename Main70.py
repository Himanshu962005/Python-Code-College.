# E27.Access Modifiers in Python.
class Student:
    def __init__(self):
        self._name = "Himanshu"
    def _funName(self):  # Protected Method.
        return "Himanshu Legendary Coder"
class Subject(Student):  # Inheritance Class.
    pass
obj = Subject()
obj1 = Student()
print(dir(obj))
# Calling by Object of Student Class.
print(obj._name)
print(obj._funName())
# Calling by Object of Subject Class.
print(obj1._name)
print(obj1._funName())