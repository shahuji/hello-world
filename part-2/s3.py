# Get the value a from below list

list1 = [1, 2, (3, 4), (5, 6, 7), (8, {'a', 'b', 'c'})]
y = 'a'
for i in list1:
    print(i)
    if isinstance(i, tuple):
        for z in i:
            print(z)
            a = set()
            if isinstance(z, set):
                a = z
                if a.__contains__(y):
                    print("it is 'A'")

# print("Enter: ", list1)
# for i in list1:
#     print(type(i))
# print("Done")
# a = ('a', 'b', 'c')
# print(type(a))

list2 = {1, 2, 3}
list3 = ['one', 'two', 'three']

list4 = zip(list(list3), list2)

print("List 4: ", list(list4))
ls = type(list2)
print("EXIT")
