str2 = "Hello this is string and list type and operator file"
str3 = "vishal"
str4 = "shahu"

print(" Capitalize str3=", str3.capitalize())
print(" Return center string str2=", str2.center(10))
print(" Now convert into upper case str2=", str3.upper())

this_list = ["apple", "banana", "cherry", "apple", "orange", "apple"]
i = 0
for fruit in this_list:

    if "apple" == fruit:
        if i != 1:
            this_list.pop(i)
        print(" Yes, 'apple' is in the fruits list")
    i += 1
[print(x) for x in this_list]

this_list2 = [100, 50, 65, 82, 23]
this_list2.sort()
print("Sorting the list in ascending order ", this_list2)
this_list2.sort(reverse=True)
print("Sorting the list in descending order ", this_list2)


def sumRound(n):
    return abs(n - 50)


this_list3 = [100, 50, 65, 82, 23, 3, 87, 10]

