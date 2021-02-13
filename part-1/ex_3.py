n = 29
i = 0
while(True):
    x = input('Gues the no.(for exit enter "e"): ')
    if(x == 'e'):
        break
    elif(i == 7):
        print('--- Game Over ---')
        break
    else:
        x = int(x)
        if(x <= 22):
            print('Very low value')
            print(sum.__doc__, '\n ', i)
            i = sum((i, 1))
        elif(x >= 23 and x <= 28):
            print('Very close to value')
            i = i + 1
        elif(x == 29):
            print('You entered right value...')
            i = i + 1
        elif(x >= 30 and x <= 35):
            print('Little far from value')
            i = i + 1
        elif(x >= 36):
            print('Too far from value')
            i = i + 1