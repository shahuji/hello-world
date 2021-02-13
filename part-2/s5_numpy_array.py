from numpy import *

arr1 = array([[1, 2, 3, 4, 5, 6],
              [1, 2, 3, 4, 5, 6]
              ])

print(arr1.ndim)  # what dimention do array have
print(arr1.shape)  # how many column and row in array(column, row)
print(arr1.size)  # calculate the capacity of array(column * row)

# Convert mutidimention to single dimention array using flatten() fun
single_array = arr1.flatten()
print(single_array)

# Convert into 3-d array using reshape(no_of_column, no_of_row)

d2_array = arr1.reshape(3, 4)
d3_array = arr1.reshape(2, 2, 3)

print(d2_array)
print(d3_array)

# Matrices
m = matrix(arr1)
m1 = matrix('0 1 2 3 ; 4 5 6 7')
m2 = matrix('0 1 2 ; 3 4 5 ; 6 7 8')
print(type(m), "\nMatrices values\nm: \n", m, '\n\nm1: \n', m1, '\n\nm2: \n', m2)

# Getting digonal values from matrices
print("\nDigonal values of m2", diagonal(m2))

