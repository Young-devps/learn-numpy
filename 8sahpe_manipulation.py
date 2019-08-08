import numpy as np

a = np.array([  [ 2., 8., 0., 6.],
                [ 4., 5., 1., 1.],
                [ 8., 9., 3., 6.]  ])

#print(a.shape)

#print(a.ravel()) # flatten the array

a.shape = (6, 2)
#print(a.T) #transpose

print(a.resize(2, 6))

print(a.reshape(3, -1)) # automatically calculate others dimension for -1

"""See also
ndarray.shape, reshape, resize, ravel
"""
