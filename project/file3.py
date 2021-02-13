print("\u2192 \N{rightwards arrow}", "List Operations...")

list1 = [12, 13, 55, 12, 67, 89, 55, 38, 13]
set1 = set()

for x in list1:
    if x not in set1:
        set1.add(x)

    else:
        print(x, " is repeat")

list1 = list(set1)
list1.sort()
print(list1)

list2 = ['abc', '23446', 'aba', 'weyw', '1221']

for x in list2:

    if len(x) > 2 and x[0] == x[-1]:
        print(x)
