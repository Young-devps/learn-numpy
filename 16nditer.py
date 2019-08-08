"""Nditer Methods and functions
nditer means opearion on each value
"""

import numpy as np


a = np.array([[0,1,4,9], 
                [0,1,4,9], 
                [0,1,4,9]])


b = np.arange(3,19,5).reshape(4,1)

for row in a:
    for value in row:
        print(value)
#same 
for cell in a.flattern():
    print(cell)

for x in np.nditer(a, order='C'):
    print(x) # can change to Fortran order


for x in np.nditer(a, order='F', flags=['external_loop']):
    print(x) # print column by columns


for x in np.nditer(a, op_flags=['readwrite']):
    x[...]=x*x

print(a)  # replace each value by the square 

for x,y in np.nditer([a, b]):
    print(x, y)