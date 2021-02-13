import sys
import re
# 10-02-21(WED)(Student Management (CRUD))
#
# Task 2: Student Management (CRUD)
#         - show each details related to result and student like:
#           enrollment number, name, email, semester, branch,
#           total subject, subject name, subject marks, total marks,
#           obtain marks, percentage, grade
#
#         - base on above student details generate marksheet
# student_data = {"student_id" : {"enroll" : "", "name", "email", "semester", "branch",
#                                  "subject" : {total 5 subject only fields(subject_name, subject_marks, total_marks, obtain_marks)}
#                                  , "percentage", "grade"}
#                  }
viewOptions = ['0. Exit ', '1. View ', '2. Add ', '3. Update ', '4. Delete ']
student_data = dict()
idSet = set()
SubjectLength = 5
enroll = 1001


def viewStudent():
    print("---> View Student <---")
    for students in student_data:
        print("----------------------------------------")
        for key, value in student_data[students].items():
            print(key, " : ", value)
        print("----------------------------------------")

    whileLoop()  # Calling main loop



def addStudent():
    """AddEmploye() function for adding employes"""
    global enroll
    print("---> Add Student <---")
    i = 1
    tempStudent = {'enrollment': enroll}
    idSet.add(enroll)

    print("Enter Student name: ")
    inputByUser = input()  # Getting student name
    while True:
        if inputByUser == "":
            print("Name must not empty")
            inputByUser = input()
        elif len(inputByUser) > 8:
            print("Name length between 2 to 8.\nEnter student name")
            inputByUser = input()
        elif len(inputByUser) <= 2:
            print("Name length must be more than 2.\nEnter student name")
            inputByUser = input()
        elif not inputByUser.isalpha():
            print("Name only contain characters.\nEnter student name")
            inputByUser = input()
        else:
            tempStudent["name"] = inputByUser.lower().capitalize()
            break

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    inputByUser = input("Enter student email\n")  # Getting student email
    while True:
        if inputByUser == '':
            print("Email must not empty.\n Enter student email")
            inputByUser = input()
        elif not re.search(regex, inputByUser):
            print("Not proper email format.\n Enter student email")
            inputByUser = input()
        else:
            tempStudent["email"] = inputByUser
            break

    inputByUser = input("Enter student semester:\n")
    while True:
        if inputByUser == '':
            print("Choice must be in digit.\n Enter student choice for semester\n")
            inputByUser = input()
        elif not inputByUser.isdigit():
            print("Choice length is 1.\n Enter student choice for semester\n")
            inputByUser = input()
        elif len(inputByUser) > 1:
            print("Choice must not empty.\n Enter student choice for semester\n")
            inputByUser = input()
        else:
            tempStudent["student"] = int(inputByUser)
            break

    inputByUser = input("Enter student branch: \n")
    while True:
        if len(inputByUser) > 12:
            print("Branch length between 5 to 12.\n Enter student branch: \n")
            inputByUser = input()
        elif len(inputByUser) <= 5:
            print("Branch length must be 5.\n Enter student branch: \n")
            inputByUser = input()
        elif inputByUser == "":
            print("Branch must not empty")
            inputByUser = input("Enter student branch: \n")
        else:
            tempStudent["branch"] = inputByUser.lower().capitalize()
            break

    student_data["studentId_" + str(enroll)] = tempStudent
    enroll += 1

    whileLoop()  # Calling main loop


def updateStudent():
    pass


def deleteStudent():
    pass



def whileLoop():
    for views in viewOptions:
        print(views, end='')
    inputByUser = input("\nEnter Your choice:\n\u2192 \N{rightwards arrow} ")
    if int(inputByUser) == 0:
        print("--------------")
        print("---> EXIT <---")
        print("--------------")
        sys.exit()
    elif int(inputByUser) == 4:
        deleteStudent()
    elif int(inputByUser) == 3:
        updateStudent()
    elif int(inputByUser) == 2:
        print("1. Add Student  2. Add Subject")

        addStudent()
    elif int(inputByUser) == 1:
        if not student_data:
            print("ADD student data then view")
            addStudent()

        print("1. View Student  2. View Subject")
        inputByUser = input()
        while True:
            if inputByUser == '':
                print("Choice must be in digit.\n Enter choice for view\n")
                inputByUser = input()
            elif not inputByUser.isdigit():
                print("Choice length is 1.\n Enter choice for view\n")
                inputByUser = input()
            elif len(inputByUser) > 1:
                print("Choice must not empty.\n Enter choice for view\n")
                inputByUser = input()
            elif int(inputByUser) > 2:
                print("Choice are only 1 and 2.\n Enter choice for view\n")
                inputByUser = input()
            else:
                break

        viewStudent()
    else:
        print("Wrong input...")
        whileLoop()

whileLoop()