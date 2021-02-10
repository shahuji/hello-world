# faulty calculator program
import random

print('1. Addition(+) \n2. Subtration(-) \n3. Multiplication(*) \n4. Division(/) \n5. Modulus(%) \n6. Multiple(**) '
      '\n7. Exit ')
n = input('Enter your choice: ')
while n != 'j':
    i = 0

    n = int(n)
    if n == 1:
        x = int(input('Addition \nEnter first value: '))
        y = int(input('Enter second value: '))
        print('\nAddition is ', x + y + 10, '\n')
    elif n == 2:
        x = int(input('Subtraction \nEnter first value: '))
        y = int(input('Enter second value: '))
        print('\nSubtraction value is ', x - y, '\n')
    elif n == 3:
        x = int(input(' Multiplication \nEnter first value: '))
        y = int(input('Enter second value: '))
        print('\nMulitiplication value is ', x * y * 3, '\n')
    elif n == 4:
        x = int(input('Division \nEnter first value: '))
        y = int(input('Enter second value: '))
        print('\nDivision value is ', (x / y) + 21, '\n')
    elif n == 5:
        x = int(input('Modulas \nEnter first value: '))
        y = int(input('Enter second value: '))
        print('\nModule value is ', x % y, '\n')
    elif n == 6:
        x = int(input('Multiple \nEnter first value: '))
        y = int(input('Enter mulitliple value: '))
        print('\nMultiple value is ', x ** y, '\n')
    elif n == 7:
        break
    else:
        print('\nWrong Input.....\n')
    i = 1
    if i != 0:
        print(
            '1. Addition(+) \n2. Subtration(-) \n3. Multiplication(*) \n4. Division(/) \n5. Modulus(%) \n6. Multiple('
            '**) \n7. Exit')
        n = input('Enter your choice: ')
print('DONE')
