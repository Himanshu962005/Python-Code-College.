# M7.Use Conditional Statements and Different Type of Loops Based on Simple Example/s.
num = 10
# Conditional Statements.
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
# For Loop.
print("For Loop :")
for i in range(1, 6):
    print(i)
# While Loop.
print("While Loop :")
i = 1
while i <= 5:
    print(i)
    i += 1
# Break and Continue.
print("Break and Continue :")
for i in range(1, 11):
    if i == 5:
        continue
    if i == 9:
        break
    print(i)