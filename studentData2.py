import sys
import re

# 11-02-21(WED)(Student Management (CRUD))
#
# Task 2: Student Management (CRUD)
#         - show each details related to result and student like:
#           enrollment number, name, email, semester, branch,
#           total subject, subject name, subject marks, total marks,
#           obtain marks, percentage, grade
#
#         - base on above student details generate marksheet
# student_data = {"student_id" : {"enroll" : "", "name", "email", "semester", "branch",
#                                  "subject" : {total 5 subject only fields(subject_name, subject_marks, obtain_marks)}
#                                   ,"total_marks", "percentage", "grade"}
#                  }
viewOptions = ['0. Exit ', '1. View ', '2. Add ', '3. Update ', '4. Delete ']
student_data = dict()
idSet = set()
SubjectLength = 6
enroll = 1001


def viewStudent():
    print("----> View Student <----")
    for students in student_data:
        print("----------------------------------------")
        for key, value in student_data[students].items():
            print(key, " : ", value)
        print("----------------------------------------")


def addStudent():
    """AddStudent() function for adding Student"""
    global enroll
    print("---> Add Student <---")
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
            print("Choice must not empty.\n Enter student choice for semester")
            inputByUser = input()
        elif not inputByUser.isdigit():
            print("Choice must be in digit.\n Enter student choice for semester")
            inputByUser = input()
        elif len(inputByUser) > 1:
            print("Choice length is 1.\n Enter student choice for semester")
            inputByUser = input()
        else:
            tempStudent["semester"] = int(inputByUser)
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
    viewStudent()
    print("--------------------------------------")
    print("---> Select id you want to update <---")
    print("All student ids: ")
    print(idSet)
    print("--------------------------------------")
    student_id = input()
    while True:
        if student_id == '':
            print("Value must not empty.\nEnter student choice for id")
            student_id = input()
        elif not student_id.isdigit():
            print("Value must be in digit.\nEnter student choice for id")
            student_id = input()
        elif len(student_id) > 4:
            print("Value length must be 4.\nEnter student choice for id")
            student_id = input()
        elif int(student_id) not in idSet:
            print("Value not exit.\nEnter student choice for id")
            student_id = input()
        else:
            break
    print("Enter the field number to update")
    print("1. Name    2. Email    3. Semester    4. Branch")
    studentField = input()
    while True:
        if studentField == '':
            print("Choice must not empty.\nEnter student choice for studentField")
            studentField = input()
        elif not studentField.isdigit():
            print("Choice must be in digit.\nEnter student choice for studentField")
            studentField = input()
        elif len(studentField) > 1:
            print("Choice length is 1.\nEnter student choice for studentField")
            studentField = input()
        elif int(studentField) not in (1, 2, 3, 4):
            print("Choice are only 4.\nEnter student choice for studentField")
            studentField = input()
        else:
            break

    if studentField == "1":
        studentField = "name"
    elif studentField == "2":
        studentField = "email"
    elif studentField == "3":
        studentField = "semester"
    else:
        studentField = "branch"

    print("Old data of \"{}\" is \"{}\".\nEnter New Data: ".format(studentField.capitalize(),
                                                                   student_data["studentId_" + student_id][
                                                                       studentField]))
    tempStudent = input()
    student_data["studentId_" + student_id][studentField] = tempStudent
    whileLoop()


def deleteStudent():
    viewStudent()
    print("--------------------------------------")
    print("---> Select id you want to delete <---")
    print("All student ids: ")
    print(idSet)
    print("--------------------------------------")
    student_id = input()
    while True:
        if student_id == '':
            print("Value must not empty.\nEnter student choice for id")
            student_id = input()
        elif not student_id.isdigit():
            print("Value must be in digit.\nEnter student choice for id")
            student_id = input()
        elif len(student_id) > 4:
            print("Value length must be 4.\nEnter student choice for id")
            student_id = input()
        elif int(student_id) not in idSet:
            print("Value not exit.\nEnter student choice for id")
            student_id = input()
        else:
            break

    print(student_data["studentId_" + student_id])
    print("-----------------------------------------")
    for key, value in student_data["studentId_" + student_id].items():
        print(key, " : ", value)
    print("------------STUDENT--DELETED-------------")
    del student_data["studentId_" + student_id]


def addSubjectData(student_id):
    flag = False
    tempSubject = dict()
    tempSubjectD = dict()
    noOfSubject = 0
    # for check in student_data:
    #     if "subject" in student_data[check]:
    if "subject" in student_data["studentId_" + student_id]:
        flag = True
        tempSubjectD = student_data["studentId_" + student_id]["subject"]
        print(tempSubjectD)
        noOfSubject = len(tempSubjectD)
        print(noOfSubject)
    else:
        student_data["studentId_" + student_id]["subject"] = dict()

    if noOfSubject < 5:
        for count in range(noOfSubject + 1, SubjectLength):
            # Getting student subject name
            print("Enter subject name: ")
            subjectName = input()
            subjectName = subjectName.strip()
            while True:
                if len(subjectName) > 2 and subjectName.replace(" ", "").isalpha():
                    tempSubject["subject name"] = subjectName.lower()
                    break
                else:
                    print("Value is invalid.\nEnter subject name: ")
                    subjectName = input().strip()

            # getting input of subject marks
            tempSubject["Marks"] = 100
            # getting input of subject marks obtain
            subjectObtainMark = input("Enter marks obtain in subject: \n")
            while True:
                if subjectObtainMark.isdigit() and (0 <= int(subjectObtainMark) or int(subjectObtainMark) <= 100):
                    tempSubject["Obtain Marks"] = subjectObtainMark
                    break
                else:
                    print("Value is invalid.\nEnter marks obtain in subject: ")
                    subjectObtainMark = input()

            # Viewing subject details
            print("Student Id: studentId_", student_id)
            print("And Data\n", student_data["studentId_" + student_id])
            # for k, v in tempSubject.items():
            #     print(k, ' : ', v)
            #     print("")
            if flag:
                print("update")
                tempSubjectD[count] = tempSubject
                print(tempSubjectD)
            else:
                print("without")
                student_data["studentId_" + student_id]["subject"][count] = tempSubject
            tempSubject = dict()
            if count <= 4:
                print("Want to add more subject results?\nEnter n for exit.")
                inputByUser = input()
                if inputByUser in ('n', 'N'):
                    break
            else:
                print("Last subject added")
    else:
        print("You already have 5 subjects.")
    if flag:
        print(tempSubjectD)
        del student_data["studentId_" + student_id]["subject"]
        student_data["studentId_" + student_id]["subject"] = tempSubjectD
        print( student_data["studentId_" + student_id]["subject"])


def addSubject():
    print("-----> Add Subject <-----")
    viewStudent()
    print("--------------------------------------")
    print("---> Select id you want to add subject <---")
    print("All student ids: ")
    print(idSet)
    print("--------------------------------------")
    student_id = input()
    while True:
        if student_id.isdigit() and int(student_id) in idSet:
            break
        else:
            print("Value not exit.\nEnter student choice for id")
            student_id = input()
    if "subject" in student_data["studentId_" + student_id]:
        print("Sorry you can not add from here...\nYou already have subject")
        updateAddSubject()
    addSubjectData(student_id)

    whileLoop()


def grade(studentPercentage):
    studentPercentage = int(studentPercentage)
    if 91 <= studentPercentage <= 100:
        return "O"
    elif 81 <= studentPercentage <= 90:
        return "A"
    elif 71 <= studentPercentage <= 80:
        return "B"
    elif 61 <= studentPercentage <= 70:
        return "C"
    elif 51 <= studentPercentage <= 60:
        return "D"
    elif 41 <= studentPercentage <= 50:
        return "E"
    else:
        return "f"


def gettingIdForSubject():
    # checking students having subject report(result)
    studentHavingSubject = set()
    for check in student_data:
        if "subject" in student_data[check]:
            studentHavingSubject.add(int(student_data[check]["enrollment"]))

    if not studentHavingSubject:
        print("------------------------------------------")
        print("None of the student having subject report.")
        print("------------------------------------------")
        whileLoop()

    for check in student_data:
        if int(student_data[check]["enrollment"]) in studentHavingSubject:
            print("----------------------------------------")
            print("Enrollment: ", student_data[check]["enrollment"], "  ", "Name: ", student_data[check]["name"])
            print("----------------------------------------")
    print("---> Select id you want to get result <---")
    print("All student ids: ")
    print(studentHavingSubject)
    print("--------------------------------------")
    student_id = input()
    while True:
        if student_id.isdigit() and int(student_id) in idSet:
            break
        else:
            print("Value not exit.\nEnter student choice for id")
            student_id = input()
    return student_id


def viewStudentResult():
    student_id = gettingIdForSubject()
    studentResult = student_data["studentId_" + student_id]["subject"]
    formatList = list(studentResult[1].keys())  # getting all fields name
    # totalMarks = int()
    totalObtainMarks = 0
    for data in studentResult:
        # totalMarks = totalMarks + int(studentResult[data]["Marks"])
        totalObtainMarks = totalObtainMarks + int(studentResult[int(data)]["Obtain Marks"])
    studentPercentage = totalObtainMarks / len(studentResult.keys())
    totalMarks = 100*len(studentResult.keys())
    studentGrade = grade(studentPercentage)

    for students in student_data:
        if students == "studentId_" + student_id:
            print("--------------------------------------------------")
            for key, value in student_data[students].items():
                if key == "subject":
                    break
                print(key, " : ", value)
            print("--------------------------------------------------")

    print("--------------------------------------------------")
    print(formatList[0], "------", formatList[1], "------", formatList[2])
    for data in studentResult:
        subjectValues = list(studentResult[data].values())
        print(subjectValues[0], "------", subjectValues[1], "------", subjectValues[2])
    print("--------------------------------------------------")
    print("TOTAL------ {} ------- {} ----------------------".format(totalMarks, totalObtainMarks))
    print("Percentage: \"{}\"".format(studentPercentage))
    print("Garde: \"{}\"".format(studentGrade))

    whileLoop()


def updateAddedSubject():
    student_id = gettingIdForSubject()
    studentResult = student_data["studentId_" + student_id]["subject"]
    formatList = list(studentResult[1].keys())  # getting all fields name
    print("id", formatList[0], "------", formatList[1], "------", formatList[2])
    # subjectKeys = list(studentResult.keys())
    for data in studentResult:
        subjectValues = list(studentResult[data].values())
        print(data, subjectValues[0], "------", subjectValues[1], "------", subjectValues[2])
    subjectId = input()
    print("1. Change Subject Name    2. Change Subject Obtain Marks")
    inputChoice = input()
    if inputChoice == "1":
        subjectName = input("Enter change subject name: \n")
        subjectName = subjectName.strip()
        while True:
            if len(subjectName) > 2 and subjectName.replace(" ", "").isalpha():
                student_data["studentId_" + student_id]["subject"][subjectId]["subject name"] = subjectName
                print("-----> Subject name changed <-----")
                break
            else:
                print("Value is invalid.\nEnter subject name: ")
                subjectName = input().strip()
    else:
        subjectObtainMark = input("Enter change marks obtain in subject: \n")
        while True:
            if subjectObtainMark.isdigit() and (0 <= int(subjectObtainMark) or int(subjectObtainMark) <= 100):
                student_data["studentId_" + student_id]["subject"][int(subjectId)]["Obtain Marks"] = subjectObtainMark
                print("-----> Subject marks changed <-----")
                break
            else:
                print("Value is invalid.\nEnter marks obtain in subject: ")
                subjectObtainMark = input()
    whileLoop()


def updateAddSubject():
    student_id = gettingIdForSubject()
    addSubjectData(student_id)


def deleteSubject():
    student_id = gettingIdForSubject()
    studentResult = student_data["studentId_" + student_id]["subject"]
    formatList = list(studentResult[1].keys())  # getting all fields name
    print("id", formatList[0], "------", formatList[1], "------", formatList[2])
    for data in studentResult:
        subjectValues = list(studentResult[data].values())
        print(data, subjectValues[0], "------", subjectValues[1], "------", subjectValues[2])
    subjectId = input()
    del student_data["studentId_" + student_id]["subject"][int(subjectId)]


def whileLoop():
    print("\n")
    for views in viewOptions:
        print(views, end='')
    inputByUser = input("\nEnter Your choice:\n\u2192 \N{rightwards arrow} ")
    while True:
        if inputByUser in {"0", "1", "2", "3", "4"}:
            break
        else:
            print("Choice are only 1 and 2.\n Enter choice for view\n")
            inputByUser = input()
    if int(inputByUser) == 0:
        print("--------------")
        print("---> EXIT <---")
        print("--------------")
        sys.exit()
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
            deleteStudent()
        else:
            deleteSubject()

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
            updateStudent()
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
                updateAddSubject()
            else:
                updateAddedSubject()

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
            addStudent()
        else:
            addSubject()

    elif int(inputByUser) == 1:
        if not student_data:
            print("ADD student data then view")
            addStudent()

        print("1. View Student    2. View Student Result")
        inputByUser = input()
        while True:
            if int(inputByUser) in {1, 2}:
                break
            else:
                print("Choice are only 1 and 2.\n Enter choice for view\n")
                inputByUser = input()
        if inputByUser == "1":
            viewStudent()
        else:
            viewStudentResult()
        whileLoop()
    else:
        print("Wrong input...")
        whileLoop()


whileLoop()
