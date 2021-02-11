# 09-FEB-2021(TUE)
# TASK student basic insert, view, update and delete

import sys

i, enroll = 0, 3
viewOptions = ['0. Exit ', '1. View ', '2. Add ', '3. Update ', '4. Delete ']
idSet = {1, 2}
desigination = (
    'Python Dev. ', 'Java Dev. ', 'Node Js. Dev. ', 'Angular Dev. ', 'Team Lead ', 'Project Manager ',
    'CEO')
employeFormat = ['Id', 'name', 'phone', 'email', 'desigination', 'experience', 'address']
employeName = [{'Id': '1', 'name': 'Vishal', 'phone': '1234567890', 'email': 'vishal@mail.com', 'desigination': '0',
                'experience': 'Fresher', 'address': 'Ahmedabad'},
               {'Id': '2', 'name': 'Happy', 'phone': '1234567891', 'email': 'happy@mail.com', 'desigination': '1',
                'experience': 'Fresher', 'address': 'Junagard'}]

inputByUser = ''


def viewCode():
    print('ID   NAME    NUMBERS    EMAIL@mail.com   Desi.   Exper   Address')
    for employs in employeName:
        print('')
        i = 0
        for data in employs:
            if i == 4:
                print(desigination[int(employs[data])], '  ', end='')
            else:
                print(employs[data], '  ', end='')
            i += 1


def view():
    """View() function for viewing employes details"""
    print("---> View Mode <---")
    viewCode()

    # print(employeNameBase)
    whileLoop()


def addEmploye():
    """AddEmploye() function for adding employes"""
    global enroll
    print("---> Add Employs <---")
    i = 1
    tempEmploye = {'Id': count}
    idSet.add(count)
    for employe in employeFormat:
        if i == 1:
            i += 1
            continue
        else:
            print("Enter the student {}:".format(employe))
            if employe == 'desigination':
                jCount = 0
                for design in desigination:
                    print(jCount + 1, '. ', design, end='')
                    jCount += 1
                print("\nEnter your choice:")
                inputByUser = int(input()) - 1
                tempEmploye[employe] = inputByUser
                continue

            inputByUser = input()
            tempEmploye[employe] = inputByUser
            i += 1
    i = 0
    for data in tempEmploye.values():
        if i == 4:
            print(desigination[int(data)], '  ', end='')
        else:
            print(data, '  ', end='')
        i += 1
    employeName.append(tempEmploye)
    count += 1
    whileLoop()


def updateEmploye():
    """UpdateEmploye() function for updating employes details"""
    # employeName[Index_value][key]=3
    print("---> Update Employs <---")
    viewCode()
    print("\n---> Select Detail <---")
    print("\nEnter ID of student:")
    employeId = int(input())
    index = 0
    # Getting Employes IDs
    for emply in employeName:
        if int(emply['Id']) == employeId:
            print("INDEX", index, end='')
            print(" ID", emply['Id'])
            break
        index += 1

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

    print("Old detail ({}) enter new detail:".format(employeName[index][employeField]))
    inputByUser = input()
    employeName[index][employeField] = inputByUser
    whileLoop()


def deleteEmploye():
    """DeleteEmploye() functions for deleting employes data"""
    print("---> Delete Employs <---")
    viewCode()
    print("\n---> Select Detail <---")
    print("\nEnter ID of student:")
    print(idSet)
    employeId = int(input())
    index = 0
    for emply in employeName:
        if int(emply['Id']) == employeId:
            print(index)
            break
        index += 1

    # print("Deleting student details are:\n{}".format())
    employs = employeName[index]
    i = 0
    for employe in employeFormat:
        print(employe, " ", end='')
    print('')
    for data in employs:
        if i == 4:
            print(desigination[int(employs[data])], '  ', end='')
        else:
            print(employs[data], '  ', end='')
        i += 1
    print("Employ -- DELETED --")
    del employeName[index]
    whileLoop()


def whileLoop():
    print("\n")
    for views in viewOptions:
        print(views, end='')
    inputByUser = input("\nEnter Your choice:\n\u2192 \N{rightwards arrow} ")
    if int(inputByUser) == 0:
        print("--------------")
        print("---> EXIT <---")
        print("--------------")
        sys.exit()
    elif int(inputByUser) == 4:
        deleteEmploye()
    elif int(inputByUser) == 3:
        updateEmploye()
    elif int(inputByUser) == 2:
        addEmploye()
    elif int(inputByUser) == 1:
        view()
    else:
        print("Wrong input...")
        whileLoop()


whileLoop()
