from array import *

"""
Delete an element from array without inbuilt function
and also reverse the array
"""

arr = array('i', [])
length = int(input("Enter the length of array: "))

for i in range(length):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)

val = int(input("Enter the number you want to delete: "))

for (place, e) in enumerate(arr):
    print(place, e)
    if e == val:
        arr = arr[0:place] + arr[place + 1:]

print(arr)
arr1 = arr[::-1]  # without using inbuilt method storing in reverse order
print(arr1)
