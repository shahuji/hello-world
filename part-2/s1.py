#
# import operator
# print('practical 1')
#
# print("Hello World")
#
# dict = {3: 40, 1: 20, 4: 50, 2: 30, 0: 10}
# print("before editing dict => ", dict)
# dict1 = sorted(dict.items(), key=operator.itemgetter(1), reverse=False)
# print('after editing in ascending order dict => ', dict1)
# dict2 = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
# print('after editing dictionary in descending order => ', dict2)

# print('practical 2')
# d1 = {0: 1, 1: 2}
# d2 = {2: 3, 3: 4}
# d3 = {4: 5, 5: 6}
# d4 = {}
# for i in (d1, d2, d3): d4.update(i)
#
# print('=> d1: ', d1, '\j=> d2: ', d2, '\j=> d3: ', d3, '\j=> d4: ', d4)

# import math
# from builtins import range
#
# print('practical 3')
# j = int(input("Enter the no.(1 to 9) :"))
# d5 = dict()
# for i in range(j + 1):
#     d5[i] = int(math.pow(float(i), 2))
#
# print(d5)

# print("Practical 4")
# keys = ['red', 'green', 'blue']
# values = ['#FF0000', '#008000', '#0000FF']
# d6 = dict(zip(keys, values))
# print(d6, "\nNow in sorted form")
# for i in sorted(d6):
#     print('%s: %s' % (i, d6[i]))

# from collections import Counter
#
# item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item3', 'amount': 750}]
# d7 = Counter()
# for d in item_list:
#     d7[d['item']] += d['amount']
#
# print("Dictionary from list => ", d7)

# Merging to dictionary using ** notation for **kwargs
# p1 = {"X": 100, "Y": 200, "Z": 300}
# p2 = {"A": 10, "B": 20, "C": 30}
# p3 = {**p1, **p2}
#
# print(p3)

# Array start
# import array as arr
#
# a = arr.array('i', [1, 2, 3])
# for i in range(0, 3):
#     print(a[i], end=" ")
#
# print('\nend')
#
# a.insert(1, 4)
# for i in range(0, 3):
#     print(a[i], end=" ")
#
# a.insert(1, 2)
# a.insert(2, 3)
# print("")
#
# for i in range(0, 3):
#     print(a[i], end=" ")
#
# a.append(5)
# for i in range(0, 3):
#     print(a[i], end=" ")
# print()

# try catch handle
# while True:
#     try:
#         a1 = int(input("Input a number: "))
#         break
#     except ValueError:
#         print("\nThis is not a number. Try again...", ValueError)
#         print()
