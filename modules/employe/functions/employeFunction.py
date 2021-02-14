
import re

i, count = 0, 1
idSet = set()
desigination = (
    'Python Dev. ', 'Java Dev. ', 'Node Js. Dev. ', 'Angular Dev. ', 'Team Lead ', 'Project Manager ',
    'CEO', 'Director')
employeFormat = ['Id', 'name', 'phone', 'email', 'desigination', 'experience', 'address']
employeName = dict()

inputByUser = ""


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
        addEmploye()
    else:
        viewCode()


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
                inputByUser = input("Enter employe choice for {}\n".format(employe))
                while True:
                    if inputByUser.isdigit() and len(inputByUser) == 1:
                        tempEmploye[employe] = int(inputByUser) - 1
                        break
                    else:
                        print("Choice length is 1.\n Enter employe choice for {}\n".format(employe))
                        inputByUser = input()
                        
            # input validation for Name
            elif employe == 'name':
                inputByUser = input("Enter employe {}\n".format(employe))
                while True:
                    if inputByUser.isalpha() and len(inputByUser) <= 10 and len(inputByUser) >= 1:
                        tempEmploye[employe] = inputByUser.lower().capitalize()
                        break
                    else:
                        print("Name only contain characters.\nEnter employe {}".format(employe))
                        inputByUser = input()
                        
            # input validation for Phone
            elif employe == 'phone':
                inputByUser = input("Enter employe {}\n".format(employe))
                while True:
                    if inputByUser.isdigit() and len(inputByUser) == 10:
                        tempEmploye[employe] = inputByUser
                        break   
                    else:
                        print("Phone no length 10.\n Enter employe {}".format(employe))
                        inputByUser = input()

            # input validation for email
            elif employe == 'email':
                regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                inputByUser = input("Enter employe {}\n".format(employe))
                while True:
                    if re.search(regex, inputByUser):
                        tempEmploye[employe] = inputByUser
                        break
                    else:
                        print("Not proper email format.\n Enter employe {}".format(employe))
                        inputByUser = input()

            # input validation for experience
            elif employe == 'experience':
                inputByUser = input("Enter employe choice for {}\n".format(employe))
                while True:
                    if inputByUser.isdigit() and len(inputByUser) == 1:
                        tempEmploye[employe] = int(inputByUser)
                        break
                    else:
                        print("Choice must be in digit.\n Enter employe choice for {}".format(employe))
                        inputByUser = input()
                        
            # input validation for address
            elif employe == 'address':
                inputByUser = input("Enter employe {}\n".format(employe))
                while True:
                    if len(inputByUser) >= 5 and len(inputByUser) <= 12:
                        tempEmploye[employe] = inputByUser.lower().capitalize()
                        break
                    else:
                        print("Address length between 5 to 12.\n enter employe {}".format(employe))
                        inputByUser = input()

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
            desigination[int(employeName["employeId_" + employeId][employeField])]))
        jCount = 0
        for design in desigination:
            print(jCount + 1, '. ', design, end='')
            jCount += 1
        print('')
        inputByUser = str(int(input())-1)
    else:
        print(employeName["employeId_" + employeId][employeField])
        print("Old detail ({}) enter new detail:".format(employeName["employeId_" + employeId][employeField]))
        inputByUser = input()
    employeName["employeId_" + employeId][employeField] = inputByUser


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
        elif employeId.isdigit() and int(employeId) in idSet:
           break
        else:
            print("Employe id not found try again.\n Enter student ID.")
            employeId = input()

    i = 0
    for employe in employeFormat:
        print(employe, " ", end='')
    print('')
    for data, value in employeName["employeId_" + employeId].items():
        if i == 4:
            print(data, ' : ', desigination[int(value)])
        else:
            print(data, ' : ', value)
        i += 1
    print("\n--> Employ -- DELETED <--")
    del employeName["employeId_" + employeId]
