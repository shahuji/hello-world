# stu = {"1":{"1":"1","2":"2","3":"3","4":"4","5":"5"},"2":"2","3":"3","4":"4","5":"5"}
# idSet = {"1":"1","2":"2","3":"3","4":"4","5":"5"}

# stu["1"]["6"] = dict()
# stu["1"]["6"]["1"] = idSet
# stu["1"]["6"]["2"] = idSet
# print("--------------------------------------")
# print("---> Select id you want to update <---")
# print("All student ids: ")
# print("--------------------------------------")
# for s, v in stu.items():
#   print(s, " : ", v)
# print("--------------------------------------")
# subjectMark = 100
# while True:
#   n = int(input("enter a number between 0 and 100: "))
#   if 0 <= n <= subjectMark:
#       break
#   print('try again')

# for count in range(0,5):
#   print(count)

# student_id = input()
# while True:
#   if student_id.isdigit() and int(student_id) == 100:
#     print(student_id)
#     break
#   else:
#     print("Name only contain characters.\nEnter subject name")
#     student_id = input()

# thisdict = {1: {"brand": "Ford",
#                 "model": "Mustang"}, 2: {"brand": "Ford",
#                                          "model": "Mustang"},
#             3: {"brand": "Ford",
#                 "model": "Mustang",
#                 }
#             }
#
# y = set()
#
# for x in thisdict:
#     if "year" in thisdict[x]:
#         y.add(thisdict[x]["year"])
#         print("NOT find")
#
# if len(y) == 0:
#     print("Zero")
#
# xdict = list(thisdict[1].values())
# # list(thisdict)
# print(xdict, y)

# addSubject()
# for count in range(1, SubjectLength):
#
#     # Getting student subject name
#     print("Enter subject name: ")
#     subjectName = input()
#     subjectName = subjectName.strip()
#     while True:
#         if len(subjectName) > 2 and subjectName.replace(" ", "").isalpha():
#             tempSubject["subject name"] = subjectName.lower()
#             break
#         else:
#             print("Value is invalid.\nEnter subject name: ")
#             subjectName = input().strip()
#
#     # getting input of subject marks
#     subjectMark = input("Enter subject marks: \n")
#     while True:
#         if subjectMark.isdigit() and int(subjectMark) == 100:
#             tempSubject["Marks"] = subjectMark
#             break
#         else:
#             print("Value is invalid.\nEnter student subject marks: ")
#             subjectMark = input()
#
#     # getting input of subject marks obtain
#     subjectObtainMark = input("Enter marks obtain in subject: \n")
#     while True:
#         if subjectObtainMark.isdigit() and (0 <= int(subjectObtainMark) or int(subjectObtainMark) <= 100):
#             tempSubject["Obtain Marks"] = subjectObtainMark
#             break
#         else:
#             print("Value is invalid.\nEnter marks obtain in subject: ")
#             subjectObtainMark = input()
#
#     # Viewing subject details
#     print("Student Id: studentId_", student_id)
#     print("And Data\n", student_data["studentId_" + student_id])
#     for k, v in tempSubject.items():
#         print(k, ' : ', v)
#         print("")
#
#     student_data["studentId_" + student_id]["subject"][count] = tempSubject
#     tempSubject = dict()
#
#     if count < 4:
#         print("Want to add more subject results?\nEnter n for exit.")
#         inputByUser = input()
#         if inputByUser in ('n', 'N'):
#             break
#     else:
#         print("Last subject added")


# updateAddSubject()
# tempSubject = student_data["studentId_" + student_id]["subject"]
# noOfSubject = len(tempSubject.keys())
# if noOfSubject < 5:
#
#     for count in range(noOfSubject + 1, SubjectLength):
#
#         # Getting student subject name
#         print("Enter subject name: ")
#         subjectName = input()
#         subjectName = subjectName.strip()
#         while True:
#             if len(subjectName) > 2 and subjectName.replace(" ", "").isalpha():
#                 tempSubject["subject name"] = subjectName.lower()
#                 break
#             else:
#                 print("Value is invalid.\nEnter subject name: ")
#                 subjectName = input().strip()
#
#         # getting input of subject marks
#         subjectMark = input("Enter subject marks: \n")
#         while True:
#             if subjectMark.isdigit() and int(subjectMark) == 100:
#                 tempSubject["Marks"] = subjectMark
#                 break
#             else:
#                 print("Value is invalid.\nEnter student subject marks: ")
#                 subjectMark = input()
#
#         # getting input of subject marks obtain
#         subjectObtainMark = input("Enter marks obtain in subject: \n")
#         while True:
#             if subjectObtainMark.isdigit() and (0 <= int(subjectObtainMark) or int(subjectObtainMark) <= 100):
#                 tempSubject["Obtain Marks"] = subjectObtainMark
#                 break
#             else:
#                 print("Value is invalid.\nEnter marks obtain in subject: ")
#                 subjectObtainMark = input()
#
#         # Viewing subject details
#         print("Student Id: studentId_", student_id)
#         print("And Data\n", student_data["studentId_" + student_id])
#         for k, v in tempSubject.items():
#             print(k, ' : ', v)
#             print("")
#
#         student_data["studentId_" + student_id]["subject"][count] = tempSubject
#         tempSubject = dict()
#
#         if count < 4:
#             print("Want to add more subject results?\nEnter n for exit.")
#             inputByUser = input()
#             if inputByUser in ('n', 'N'):
#                 break
#         else:
#             print("Last subject added")
# else:
#     print("You already have 5 subjects.")