n = int(input('0. Upset Down \n1. Downset Up \n=> '))
if n == 0:
    print('UpSet Down!!!')
    for i in range(1, 6):
        for j in range(i):
            print('*', end=" ")
        print('\n')
else:
    print('DownSet Up!!!')
    for i in range(0, 5):
        for j in range((5 - i), 0, -1):
            print('*', end=" ")
        print('\n')

print('Hello!!!')


def getdate():
    import datetime
    return datetime.datetime.now()


print(getdate())
