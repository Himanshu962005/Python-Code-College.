# E20.Snake Water Gun in Python.
# Snake, Water, and Gun is a Variation of the Children's Game "Rock-Paper-Scissors" where Players use Hand Gestures to Represent a Snake, Water, or Gun.
# The Gun Beats the Snake, the Water Beats the Gun, and the Snake Beats the Water.
# Write a Python Program to Create a Snake Water Gun Game in Python using If-Else Statements.
# Do not Create any Fancy GUI.
# Use Proper Functions to Check for Win.
import random;
def check(comp, user):
    if comp == user:
        return 0
    if comp == 0 and user == 1:
        return -1
    if comp == 1 and user == 2:
        return -1
    if comp == 2 and user == 0:
        return -1
    return 1
comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for Water, 2 for Gun : "))
score = check(comp, user)
print("You Choose :", user)
print("Computer Choose :", comp)
if score == 0:
    print("It's a Draw.")
elif score == -1:
    print("You Lose.")
else:
    print("You Win.")