import pickle

# 10. A binary file school.dat has structure(rollno, name, class, fees)
#  Write a definition for function total_fees( ) that reads each object of file and calculate the total fees of students and display the same.


studentData = dict()


def makeFile():
    # we get dynamic data from user also....
    studentData = { 1001: {'rollno': 1003, 'name': 'DON',
                          'class': 3, 'fees': 10000},
                    1002: {'rollno': 1003, 'name': 'Vijay',
                          'class': 1, 'fees': 20000},
                    1003: {'rollno': 1003, 'name': 'Shahuji',
                          'class': 2, 'fees': 30000},
                    1004: {'rollno': 1003, 'name': 'Shufuji',
                          'class': 2, 'fees': 40000},
                    1005: {'rollno': 1005, 'name': 'Vishal',
                          'class': 1, 'fees': 80000}}

    with open('files/studentData.dat', 'wb') as dbFile:
        pickle.dump(studentData, dbFile)
        dbFile.close()
    studentData = {}


def getData():
    totalFees = int()
    with open('files/studentData.dat', 'rb') as dbFile:
        studentData = pickle.load(dbFile)

        for student in studentData:
            totalFees += studentData[student]["fees"]
    print("Total collected fees is | ", totalFees, " |")


makeFile()
getData()

