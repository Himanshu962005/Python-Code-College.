# E3.Create a Program Capable of Displaying Questions to the User Like KBC. Use List Data Type to Store the Questions and their Correct Answers. Display the Final Amount the Person is Taking Home After Playing the Game.
questions = [
    [
        "Which Language was used to Create Facebook?",
        "Python",
        "French",
        "JavaScript",
        "PHP",
        "None",
        4,
    ],
    [
        "Which Language was used to Create Instagram?",
        "Python",
        "French",
        "JavaScript",
        "PHP",
        "None",
        4,
    ],
    [
        "Which Language was used to Create Twitter?",
        "Python",
        "French",
        "JavaScript",
        "PHP",
        "None",
        4,
    ],
    [
        "Which Language is Mainly used for Android Development?",
        "Python",
        "Kotlin",
        "PHP",
        "HTML",
        "None",
        2,
    ],
    [
        "Which Company Developed the Python Programming Language?",
        "Microsoft",
        "Google",
        "Python Software Foundation",
        "Apple",
        "None",
        3,
    ],
    [
        "Which Language is used to Style HTML Webpages?",
        "Python",
        "CSS",
        "Java",
        "SQL",
        "None",
        2,
    ],
    [
        "Which Database Language is used to Manage Relational Databases?",
        "HTML",
        "CSS",
        "SQL",
        "Python",
        "None",
        3,
    ],
    [
        "What does CPU Stand for?",
        "Central Processing Unit",
        "Computer Personal Unit",
        "Central Program Utility",
        "Computer Processing User",
        "None",
        1,
    ],
    [
        "Which Company Developed the Android Operating System?",
        "Microsoft",
        "Google",
        "Apple",
        "IBM",
        "None",
        2,
    ],
    [
        "What does HTML Stand for?",
        "Hyper Text Markup Language",
        "High Technology Machine Language",
        "Hyper Transfer Machine Language",
        "Home Tool Markup Language",
        "None",
        1,
    ],
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(f"A. {question[1]} B. {question[2]}")
    print(f"C. {question[3]} D. {question[4]}")
    reply = int(input("Enter your Answer (1-4) or 0 to Quit : "))
    if reply == 0:
        if i == 0:
            money = 0
        else:
            money = levels[i - 1]
        break
    if reply == question[-1]:
        print(f"Correct Answer, You Have Won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
        else:
            money = levels[i]
    else:
        print("Wrong Answer!")
        break
print(f"Your Take Home Money is Rs. {money}")