import re
import sys

# 10-02-21(WED)(Update in yesterday program)
# all input fields are cross verifying before storing, using regular expression, string method,
# putting exit point then update version of employe data nested Dictionary, no id must repeat by using set
# final update done

i, count = 0, 1
viewOptions = ['0. Exit ', '1. View ', '2. Add ', '3. Update ', '4. Delete ']
idSet = set()
desigination = (
    'Python Dev. ', 'Java Dev. ', 'Node Js. Dev. ', 'Angular Dev. ', 'Team Lead ', 'Project Manager ',
    'CEO', 'Director')
employeFormat = ['Id', 'name', 'phone', 'email', 'desigination', 'experience', 'address']
employeName = {}

inputByUser = ""


def viewCode():
    for employs in employeName:
        print('')
        i = 0
        print(employs)
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

    whileLoop()


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
                        
    # Input end and below code is for viewing inserted employe data
    i = 0
    for data in tempEmploye.values():
        if i == 4:
            print(desigination[int(data)], '  ', end='')
        else:
            print(data, '  ', end='')
        i += 1
    employeName["employeId_" + str(count)] = tempEmploye
    count += 1
    whileLoop()


def updateEmploye():
    """UpdateEmploye() function for updating employes details"""
    # employeName[Index_value][key]=3
    print("---> Update Employs <---")
    viewCode()
    print("\n---> Select Detail <---")
    # Getting employe ID
    print("\nEnter ID of employe:")
    print(idSet)
    employeId = input("n/N for exit\n")
    while True:
        if employeId in {'n', 'N'}:
            break
        elif not employeId.isdigit():
            print("Enter correct no of employe id.\n Enter employe ID.")
            employeId = input()
        elif not int(employeId) in idSet:
            print("Employe id not found try again.\n Enter employe ID.")
            employeId = input()
        else:
            break

    # Getting Field
    jcount = 1
    for employe in employeFormat:
        print(jcount, '. ', employe, ' ', end='')
        jcount += 1
    print("\nEnter employe field name number:")
    employeField = int(input())  # getting field by number
    jcount = 1
    for employe in employeFormat:
        if jcount == employeField:
            employeField = employe  # getting field name in string
        jcount += 1
    
    print(employeName)
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
        print("Old detail ({}) enter new detail:".format(employeName["employeId_" + employeId][employeField]))
        inputByUser = input()
    employeName["employeId_" + employeId][employeField] = inputByUser
    whileLoop()


def deleteEmploye():
    """DeleteEmploye() functions for deleting employes data"""
    print("---> Delete Employs <---")
    viewCode()
    print("\n---> Select Detail <---")
    print("\nEnter ID of employe:")
    print(idSet)
    employeId = input("n/N for exit\n")
    while True:
        if employeId in {'n', 'N'}:
            break
        elif not employeId.isdigit():
            print("Enter correct no of employe id.\n Enter employe ID.")
            employeId = input()
        elif not int(employeId) in idSet:
            print("Employe id not found try again.\n Enter employe ID.")
            employeId = input()
        else:
            break

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
print("PROGRAM is existing")

