students = {"student_1": {"a": "a1", "b": "B1", "c": "c1", "subject": {"a": "sa1", "b": "SB1", "c": "sc1"}},
            "student_2": {"a": "a2", "b": "B2", "c": "c2"},
            "student_3": {"a": "a3", "b": "B3", "c": "c3", "subject": {"a": "sa3", "b": "SB3", "c": "sc3"}}}

studentLength = 5


def fun2():
    print("Entered in Insert Subject")
    for student in students:
        if "subject" in students[student]:
            print(student, " having subject whould u like to update...")
            input()
        else:
            print(student, " not having subject.")
            a = input()
            b = input()
            c = input()
            students[student]["subject"] = {"a"+"1": a, "b"+"1": b, "c"+"1": c}
            print(students[student]["subject"])


def fun3():
    pass


def fun4():
    pass


def fun1():
    print("1) Insert Subject    2). View Subject    3). Update Subject")
    print("Enter your option:")
    userInput = input()
    if userInput == "1":
        fun2()
    elif userInput == "2":
        fun3()
    elif userInput == "3":
        fun4()
    else:
        fun1()


fun1()
