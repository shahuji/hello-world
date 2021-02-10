import random as rm
# 1 == Stone
# 2 == Paper
# 3 == Sicsor
z = 0

while z <= 10:
    z += 1
    y = rm.randint(1, 3)
    print('Enter your choice:')
    x = int(input('1. Stone \n2. Paper \n3. Sicsor \n0. EXIT \n=> '))
    # 1=2,1=3,2=3,1=1,2=2,3=3
    if (x == 1 and y == 2) or (x == 2 and y == 1):
        if x == 1:
            print('Congo! you win...')
        else:
            print('Sorry, you lose...')
    elif (x == 1 and y == 3) or (x == 3 and y == 1):
        if x == 3:
            print('Congo! you win...')
        else:
            print('Sorry, you lose...')
    elif (x == 2 and y == 3) or (x == 3 and y == 2):
        if x == 2:
            print('Congo! you win...')
        else:
            print('Sorry, you lose...')
    elif (x == 1 and y == 1) or (x == 2 and y == 2) or (x == 3 and y == 3):
        print('Match DRAW...')
    elif x == 0:
        print('BYE BYE...')
        break
    else:
        print('Wrong INPUT...Try again')
print('EXIT---')