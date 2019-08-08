import numpy as np
from numpy import newaxis


a = np.floor(10*np.random.random((2,2)))

b = np.floor(10*np.random.random((2,2)))

#print(np.vstack(a))

#print(np.hstack(a, b)) # same to column_stack

a = np.array([4.,2.])

b = np.array([2.,8.])

#print(a[:, newaxis])

#print (b[:, newaxis])

print(np.column_stack((a[:,newaxis],b[:,newaxis])))

print(np.vstack((a[:,newaxis],b[:,newaxis])))
