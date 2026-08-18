# Q29.Python Program to Create a Class in Which One Method Accepts a String from the User and Another Prints it.
class Demo:
    def get_string(self):
        self.s = input("Enter String : ")
    def print_string(self):
        print("String is :", self.s)
obj = Demo()
obj.get_string()
obj.print_string()