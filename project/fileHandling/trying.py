import pickle

dict1 = dict()


def makeFile():
    # we get dynamic data from user also....
    dict1 = {1001: {'rollno': 1003, 'name': 'DON',
                    'class': 3, 'fees': 10000},
             1002: {'rollno': 1003, 'name': 'Vijay',
                    'class': 1, 'fees': 20000},
             1003: {'rollno': 1003, 'name': 'Shahuji',
                    'class': 2, 'fees': 30000},
             1004: {'rollno': 1003, 'name': 'Shufuji',
                    'class': 2, 'fees': 40000},
             1005: {'rollno': 1005, 'name': 'Vishal',
                    'class': 1, 'fees': 80000}}

    with open('files/Data.dat', 'wb') as dbFile:
        pickle.dump(dict1, dbFile)
        dbFile.close()
    dict1 = {}


makeFile()
checkValue = 0
while True:
    try:
        print("Enter your int value:")
        checkValue = int(input())
    except:
        print("Input error!")
        continue
    break
totalFees = int()
with open('files/Data.dat', 'rb') as dbFile:
    dict1 = pickle.load(dbFile)

for student in dict1:
    if checkValue == student:
        print("ID({}) {} student's fees is {}".format(student, dict1[student]["name"], dict1[student]["fees"]))
    totalFees += dict1[student]["fees"]
print("Total collected fees is | ", totalFees, " |")
