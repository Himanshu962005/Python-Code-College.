class Employee:
    def __init__(self, name):
        self.name = name
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    def __str__(self):
        return f"The Name of the Employee is {self.name} Karwa."
    def __repr__(self):
        return f"Employee('{self.name}')"
    def __call__(self):
        print("Hey! I am Good.")