from modules.employe.functions import employeFunction as empFun
import sys as s

viewOptions = ['0. Exit ', '1. View ', '2. Add ', '3. Update ', '4. Delete ']


def whileLoop():
    print("\n")
    for views in viewOptions:
        print(views, end='')
    inputByUser = input("\nEnter Your choice:\n\u2192 \N{rightwards arrow} ")
    if int(inputByUser) == 0:
        print("--------------")
        print("---> EXIT <---")
        print("--------------")
        s.exit()
    elif int(inputByUser) == 4:
        empFun.deleteEmploye()
        whileLoop()
    elif int(inputByUser) == 3:
        empFun.updateEmploye()
        whileLoop()
    elif int(inputByUser) == 2:
        empFun.addEmploye()
        whileLoop()
    elif int(inputByUser) == 1:
        empFun.view()
        whileLoop()
    else:
        print("Wrong input...")
        whileLoop()

        
whileLoop()
print("PROGRAM is existing")
