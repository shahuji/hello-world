def gtdt():
    import datetime
    return datetime.datetime.now()

def choice(x, n1, n2):
    l = 0
    y = int(input('1. Log    2. View \n=> '))
    while(l == 0):
        if (y == 1):
            log(x, n1, n2)
        elif (y == 2):
            view(x, n1, n2)
        else:
            break
        y = int(input('1. Log    2. View    3. Exit \n=> '))

def log(x, n1, n2):
    f = 0
    print('Loging into', x, 'data')
    b = int(input('1. Food eat    2. Exciese    \n=> '))
    while(f == 0):
        if(b == 1):
            with open(n1, 'a') as r:
                print('Enter the food eaten: ')
                strg = input('=> ')
                r.write('['+str(gtdt())+'] : '+ strg + '\n')
                r.close()
        elif(b == 2):
            print('Enter the exciese had done: ')
            with open(n2, 'a') as r:
                strg = input('=> ')
                r.write('[' + str(gtdt()) + '] : ' + strg + '\n')
                r.close()
        else:
            break

        b = int(
            input('Want to log more then enter \n1. Food eat    2. Exciese    3. Exit \n=> '))

def view(x, n1, n2):
    f = 0
    print('You are here for view of ', x, 'data.')
    b = int(input('1. Food eat    2. Exciese    \n=>'))
    while(f == 0):
        if(b == 1):
            with open(n1, 'r') as r:
                print(x,'had eaten food: ')
                for n in r.readlines():
                    print(n, end='')
                r.close()

        elif(b == 2):
            with open(n2, 'r') as r:
                print(x,'had done exciese: ')
                for n in r.readlines():
                    print(n, end='')
                r.close()

        else:
            break

        b = int(input('Want to view more then enter: \n1. Food eat    2. Exciese    3. Exit \n=> '))


def file(q):
    if(q == 1):
        x = 'Shahuji'
        n1 = 'x1.txt' #food file
        n2 = 'x2.txt' #exciese_file
        choice(x, n1, n2)

    elif(q == 2):
        x = 'Vishal'
        n1 = 'y1.txt' #food file
        n2 = 'y2.txt' #exciese_file
        choice(x, n1, n2)

    elif(q == 3):
        x = 'Vishu'
        n1 = 'z1.txt' #food_file
        n2 = 'z2.txt' #exciese_file
        choice(x, n1, n2)

    else:
        print('Wrong INPUT')


print('Welcome! to detail of:\n1. Shahuji(x) \n2. Vishal(y) \n3. Vishu(z)')
t = 1
a = int(input('Enter your choice: \n=> '))
while(t == 1):
    file(a)
    a = int(input('Want to more view or write: \n1. Shahuji(x) \n2. Vishal(y) \n3. Vishu(z) \n0. EXIT \n=> '))
    if(a == 0):
        t = a
        print('---EXIT---')
        break

print("")