import function.studentFunctions as stuFun
import sys as s

viewOptions = ['0. Exit ', '1. View ', '2. Add ', '3. Update ', '4. Delete ']


def whileLoop():
    print("\n")
    for views in viewOptions:
        print(views, end='')
    inputByUser = input("\nEnter Your choice:\n\u2192 \N{rightwards arrow} ")
    while True:
        if inputByUser in {"0", "1", "2", "3", "4"}:
            break
        else:
            print("Choice are only between 1 to 5.\n Enter choice for view\n")
            inputByUser = input()
    if int(inputByUser) == 0:
        print("--------------")
        print("---> EXIT <---")
        print("--------------")
        s.exit()
    elif int(inputByUser) == 4:
        print("1. Delete Student  2. Delete Student Subject")
        inputByUser = input()
        while True:
            if int(inputByUser) in {1, 2}:
                break
            else:
                print("Choice are only 1 and 2.\n Enter choice for view\n")
                inputByUser = input()
        if inputByUser == "1":
            stuFun.deleteStudent()
        else:
            stuFun.deleteSubject()
        whileLoop()

    elif int(inputByUser) == 3:
        print("1. Update Student  2. Update Student Subject")
        inputByUser = input()
        while True:
            if int(inputByUser) in {1, 2}:
                break
            else:
                print("Choice are only 1 and 2.\n Enter choice for view\n")
                inputByUser = input()
        if inputByUser == "1":
            stuFun.updateStudent()
        else:
            print("1. Add Student Subject  2. Update Added Student Subject")
            inputByUser = input()
            while True:
                if int(inputByUser) in {1, 2}:
                    break
                else:
                    print("Choice are only 1 and 2.\n Enter choice for view\n")
                    inputByUser = input()
            if inputByUser == "1":
                stuFun.addSubject(False)  #
            else:
                stuFun.updateAddedSubject()
        whileLoop()

    elif int(inputByUser) == 2:
        print("1. Add Student  2. Add Subject")
        inputByUser = input()
        while True:
            if int(inputByUser) in {1, 2}:
                break
            else:
                print("Choice are only 1 and 2.\n Enter choice for view\n")
                inputByUser = input()
        if inputByUser == "1":
            stuFun.addStudent()
        else:
            stuFun.addSubject(True)
        inputByUser = ""
        whileLoop()

    elif int(inputByUser) == 1:
        if not stuFun.student_data:
            print("ADD student data then view")
            stuFun.addStudent()

        print("1. View Student    2. View Student Result")
        inputByUser = input()
        while True:
            if int(inputByUser) in {1, 2}:
                break
            else:
                print("Choice are only 1 and 2.\n Enter choice for view\n")
                inputByUser = input()
        if inputByUser == "1":
            stuFun.viewStudent()
        else:
            stuFun.viewStudentResult()
        whileLoop()
    else:
        print("|---- Wrong input ----|")
        whileLoop()


whileLoop()