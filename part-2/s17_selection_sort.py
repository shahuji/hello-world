# Selection Sorting

def sort(cont):

    for i in range(len(cont)):
        minpos = i
        for j in range(i, len(cont)):
            if cont[j] < cont[minpos]:
                minpos = j
        temp = cont[i]
        cont[i] = cont[minpos]
        cont[minpos] = temp


content = [12, 34, 56, 78, 90, 23, 45, 67, 89, 10]
print("Before sorting: ", content)
sort(content)
print("After sorting: ", content)
