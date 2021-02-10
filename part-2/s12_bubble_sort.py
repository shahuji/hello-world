# Sorting a list

def sort(cont):

    for i in range(len(content)-1, 0, -1):
        for j in range(i):
            if cont[j] > cont[j+1]:
                temp = cont[j]
                cont[j] = cont[j+1]
                cont[j+1] = temp


content = [12, 34, 56, 78, 90, 23, 45, 67, 89]
print("Before sorting: ", content)
sort(content)
print("After sorting: ", content)

