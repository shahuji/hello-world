
import re

i, count = 0, 1
idSet = set()
desigination = (
    'Python Dev. ', 'Java Dev. ', 'Node Js. Dev. ', 'Angular Dev. ', 'Team Lead ', 'Project Manager ',
    'CEO', 'Director')
employeFormat = ['Id', 'name', 'phone', 'email', 'desigination', 'experience', 'address']
employeName = dict()

inputByUser = 0


def viewCode():
    for employs in employeName:
        print('')
        i = 0
        for data, value in employeName[employs].items():
            if i == 4:
                print(data, ' : ', desigination[int(value)])
            else:
                print(data, ' : ', value)
            i += 1


def view():
    """View() function for viewing employes details"""
    print("---> View Mode <---")
    if not employeName:
        print("First enter employs data....")
        # empMenu.whileLoop()
    else:
        viewCode()

    # empMenu.whileLoop()


def addEmploye():
    """AddEmploye() function for adding employes"""
    global count
    print("---> Add Employs <---")
    i = 1
    tempEmploye = {'Id': count}
    idSet.add(count)
    for employe in employeFormat:
        if i == 1:
            i += 1
        else:
            # input validation for Desigination
            if employe == 'desigination':
                jCount = 0
                for design in desigination:
                    print(jCount + 1, '. ', design, end='')
                    jCount += 1
                print("\nEnter your choice:")
                inputByUser = input("Enter student choice for {}\n".format(employe))
                while True:
                    if not inputByUser.isdigit():
                        print("Choice must be in digit.\n Enter student choice for {}\n".format(employe))
                        inputByUser = input()
                    elif len(inputByUser) > 1:
                        print("Choice length is 1.\n Enter student choice for {}\n".format(employe))
                        inputByUser = input()
                    elif inputByUser == '':
                        print("Choice must not empty.\n Enter student choice for {}\n".format(employe))
                        inputByUser = input()
                    else:
                        tempEmploye[employe] = int(inputByUser) - 1
                        break
            # input validation for Name
            elif employe == 'name':
                inputByUser = input("Enter student {}\n".format(employe))
                while True:
                    if inputByUser == "":
                        print("Name must not empty")
                        inputByUser = input()
                    elif len(inputByUser) > 8:
                        print("Name length between 2 to 8.\nEnter student {}".format(employe))
                        inputByUser = input()
                    elif len(inputByUser) <= 2:
                        print("Name length must be more than 2.\nEnter student {}".format(employe))
                        inputByUser = input()
                    elif not inputByUser.isalpha():
                        print("Name only contain characters.\nEnter student {}".format(employe))
                        inputByUser = input()
                    else:
                        tempEmploye[employe] = inputByUser.lower().capitalize()
                        break
            # input validation for Phone
            elif employe == 'phone':
                inputByUser = input("Enter student {}\n".format(employe))
                while True:
                    if not inputByUser.isdigit():
                        print("Phone no must be in digit.\n Enter student {}".format(employe))
                        inputByUser = input()
                    elif len(inputByUser) > 10:
                        print("Phone length between 8 to 10.\n Enter student {}".format(employe))
                        inputByUser = input()
                    elif len(inputByUser) <= 8:
                        print("Phone length between 8 to 10.\n Enter student {}".format(employe))
                        inputByUser = input()
                    elif len(inputByUser) == 9:
                        print("Phone length between 8 to 10.\n Enter student {}".format(employe))
                        inputByUser = input()
                    else:
                        tempEmploye[employe] = inputByUser
                        break
            # input validation for email
            elif employe == 'email':
                regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                inputByUser = input("Enter student {}\n".format(employe))
                while True:
                    if inputByUser == '':
                        print("Email must not empty.\n Enter student {}".format(employe))
                        inputByUser = input()
                    elif not re.search(regex, inputByUser):
                        print("Not proper email format.\n Enter student {}".format(employe))
                        inputByUser = input()
                    else:
                        tempEmploye[employe] = inputByUser
                        break
            # input validation for experience
            elif employe == 'experience':
                inputByUser = input("Enter student choice for {}\n".format(employe))
                while True:
                    if inputByUser == '':
                        print("Choice must be in digit.\n Enter student choice for {}".format(employe))
                        inputByUser = input()
                    elif not inputByUser.isdigit():
                        print("Choice length is 1.\n Enter student choice for {}".format(employe))
                        inputByUser = input()
                    elif len(inputByUser) > 1:
                        print("Choice must not empty.\n Enter student choice for {}".format(employe))
                        inputByUser = input()
                    else:
                        tempEmploye[employe] = int(inputByUser)
                        break
            # input validation for address
            elif employe == 'address':
                inputByUser = input("Enter student {}\n".format(employe))
                while True:
                    if len(inputByUser) > 12:
                        print("Address length between 5 to 12.\n enter student {}".format(employe))
                        inputByUser = input()
                    elif len(inputByUser) <= 5:
                        print("Address length must be 5.\n enter student {}".format(employe))
                        inputByUser = input()
                    elif inputByUser == "":
                        print("Address must not empty")
                        inputByUser = input("Enter student {}".format(employe))
                    else:
                        tempEmploye[employe] = inputByUser.lower().capitalize()
                        break
    # Input end and below code is for viewing inserted student data
    i = 0
    for data in tempEmploye.values():
        if i == 4:
            print(desigination[int(data)], '  ', end='')
        else:
            print(data, '  ', end='')
        i += 1
    employeName["employeId_" + str(count)] = tempEmploye
    count += 1
    # empMenu.whileLoop()


def updateEmploye():
    """UpdateEmploye() function for updating employes details"""
    # employeName[Index_value][key]=3
    print("---> Update Employs <---")
    viewCode()
    print("\n---> Select Detail <---")
    # Getting student ID
    print("\nEnter ID of student:")
    employeId = input("n/N for exit\n")
    while True:
        if employeId in {'n', 'N'}:
            break
        elif not employeId.isdigit():
            print("Enter correct no of student id.\n Enter student ID.")
            employeId = input()
        elif not int(employeId) in idSet:
            print("Employe id not found try again.\n Enter student ID.")
            employeId = input()
        else:
            break

    # Getting Field
    jcount = 1
    for employe in employeFormat:
        print(jcount, '. ', employe, ' ', end='')
        jcount += 1
    print("\nEnter student field name number:")
    employeField = int(input())  # getting field by number
    jcount = 1
    for employe in employeFormat:
        if jcount == employeField:
            employeField = employe  # getting field name in string
        jcount += 1

    if employeField == 'desigination':
        print("Old detail ({}) enter new detail:".format(
            desigination[int(employeName["employeID_" + employeId][employeField])]))
        jCount = 0
        for design in desigination:
            print(jCount + 1, '. ', design, end='')
            jCount += 1
        print('')
        inputByUser = str(int(input())-1)
    else:
        print(employeName["employeID_" + employeId][employeField])
        print("Old detail ({}) enter new detail:".format(employeName["employeID_" + employeId][employeField]))
        inputByUser = input()
    employeName["employeID_" + employeId][employeField] = inputByUser
    # empMenu.whileLoop()


def deleteEmploye():
    """DeleteEmploye() functions for deleting employes data"""
    print("---> Delete Employs <---")
    viewCode()
    print("\n---> Select Detail <---")
    print("\nEnter ID of student:")
    print(idSet)
    employeId = input("n/N for exit\n")
    while True:
        if employeId in {'n', 'N'}:
            break
        elif not employeId.isdigit():
            print("Enter correct no of student id.\n Enter student ID.")
            employeId = input()
        elif not int(employeId) in idSet:
            print("Employe id not found try again.\n Enter student ID.")
            employeId = input()
        else:
            break

    i = 0
    for employe in employeFormat:
        print(employe, " ", end='')
    print('')
    for data, value in employeName["employeID_" + employeId].items():
        if i == 4:
            print(data, ' : ', desigination[int(value)])
        else:
            print(data, ' : ', value)
        i += 1
    print("\n--> Employ -- DELETED <--")
    del employeName["employeID_" + employeId]
    # empMenu.whileLoop()
