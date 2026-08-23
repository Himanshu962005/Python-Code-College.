# E2.Create a Python Program Capable of Greeting you with Good Morning, Good Afternoon and Good Night. Your Program should Use Time Module to get the Current Hour. Here is a Simple Program and Documentation Link for you :
import time;
t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
# hour = int(input("Enter Hour : ")).
# print(hour).
if hour >= 0 and hour < 12:
    print("Good Morning Sir!.")
elif hour >= 12 and hour < 17:
    print("Good Afternoon Sir!.")
elif hour >= 17 and hour < 0:
    print("Good Night Sir!.")