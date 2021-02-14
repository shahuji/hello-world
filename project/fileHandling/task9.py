import pickle
# 9. Write a function to search and display details of student whose rollno is '1005' from the binary file student.dat
#     having structure [rollno, name, class and fees].
studentData = dict()


def makeFile():
    studentData = {1003: {'rollno': 1003, 'name': 'shufuji',
                          'class': 2, 'fees': 40000},
                   1005: {'rollno': 1005, 'name': 'Vishal',
                          'class': 1, 'fees': 80000}}

    with open('files/student.dat', 'wb') as dbFile:
        pickle.dump(studentData, dbFile)
        dbFile.close()
    studentData = {}


def getData():
    enterId = input("Enter student ID you to get fees:")
    
    with open('files/student.dat', 'rb') as dbFile:
        studentData = pickle.load(dbFile)
        while True:
            if int(enterId) not in studentData:
                enterId = input("Enter student ID you to get fees:")
            else:
                break

        for student in studentData:
            if int(enterId) == student:
                print("ID({}) {} student's fees is {}".format(student, studentData[student]["name"], studentData[student]["fees"]))


makeFile()
getData()