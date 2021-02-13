import re

student_data = dict()  # only subject key is in integer
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
        if inputByUser.isalpha() and len(inputByUser) <= 10 and len(inputByUser) >= 1:
            tempStudent["name"] = inputByUser.lower().capitalize()
            break
        else:
            print("Name only contain characters.\nEnter student name")
            inputByUser = input()

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    inputByUser = input("Enter student email\n")  # Getting student email
    while True:
        if re.search(regex, inputByUser):
            tempStudent["email"] = inputByUser
            break
        else:
            print("Not proper email format.\n Enter student email")
            inputByUser = input()

    inputByUser = input("Enter student semester:\n")
    while True:
        if inputByUser.isdigit() and len(inputByUser) >= 1 and inputByUser <= "10":
            tempStudent["semester"] = int(inputByUser)
            break
        else:
            print("Choice must be in digit and <= 10.\n Enter student choice for semester")
            inputByUser = input()

    inputByUser = input("Enter student branch: \n")
    while True:
        if inputByUser.isalpha() and len(inputByUser) >= 3 and len(inputByUser) <= 10:
            tempStudent["branch"] = inputByUser.lower().capitalize()
            break
        else:
            print("Branch name only contain characters and length between 3 to 10.")
            inputByUser = input("Enter student branch: \n")
    student_data["studentId_" + str(enroll)] = tempStudent
    enroll += 1


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
        print(student_data["studentId_" + student_id]["subject"])


def addSubject(check):
    student_id = ""
    if check:
        # AddSubject() call for add
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
    else:
        # AddSubject() call for update
        student_id = gettingIdForSubject()
        if "subject" not in student_data["studentId_" + student_id]:
            print("This student dont have any report")
    addSubjectData(student_id)


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
        return "w"


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
    formatList = list(studentResult[list(studentResult.keys())[0]].keys())  # getting all fields name remain
    # totalMarks = int()
    totalObtainMarks = 0
    for data in studentResult:
        # totalMarks = totalMarks + int(studentResult[data]["Marks"])
        totalObtainMarks = totalObtainMarks + int(studentResult[int(data)]["Obtain Marks"])
    studentPercentage = round(totalObtainMarks / len(studentResult.keys()), 2)
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
    print("---------------------RESULT-----------------------")
    print("--------------------------------------------------")
    print(formatList[0], "------", formatList[1], "------", formatList[2])
    for data in studentResult:
        subjectValues = list(studentResult[data].values())
        print(subjectValues[0], "------", subjectValues[1], "------", subjectValues[2])
    print("--------------------------------------------------")
    print("TOTAL------ {} ------- {} ----------------------".format(totalMarks, totalObtainMarks))
    print("Percentage: \"{}\"".format(studentPercentage))
    print("Garde: \"{}\"".format(studentGrade))
    print("--------------------------------------------------")


def updateAddedSubject():
    student_id = gettingIdForSubject()
    studentResult = student_data["studentId_" + student_id]["subject"]
    formatList = list(studentResult[list(studentResult.keys())[0]].keys())  # getting all fields name
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
                student_data["studentId_" + student_id]["subject"][int(subjectId)]["subject name"] = subjectName
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


def deleteSubject():
    student_id = gettingIdForSubject()
    studentResult = student_data["studentId_" + student_id]["subject"]
    formatList = list(studentResult[list(studentResult.keys())[0]].keys())  # getting all fields name
    print("id", formatList[0], "------", formatList[1], "------", formatList[2])
    for data in studentResult:
        subjectValues = list(studentResult[data].values())
        print(data, subjectValues[0], "------", subjectValues[1], "------", subjectValues[2])
    subjectId = input()
    while True:
        if int(subjectId) in list(studentResult.keys()):
            break
        else:
            subjectId = input("Subject Id is invalid...Reenter")
    del student_data["studentId_" + student_id]["subject"][int(subjectId)]

