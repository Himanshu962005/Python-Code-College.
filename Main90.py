# E47.Walrus Operator in Python.
# Walrus Operator (:=).
# New to Python 3.8.
# Assignment Expressions AKA Walrus Operator.
# Assigns Values to Variables as Part of a Larger Expression.
# happy = False.
# print(happy).
# print(happy := True).
# foods = list().
# while True:
#   food = input("What Food do you Like? : ").
#   if food == "quit":
#     break.
#  foods.append(food).
foods = list()
while (food := input("What Food do you Like? : ")) != "Quit":
    foods.append(food)