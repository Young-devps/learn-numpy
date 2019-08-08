import numpy as np

a = np.array( [20, 30, 40,50] )
b = np.arange(4)
c = a - b

#print(c)
#print(b)
#print(b**2) # square

#print(10*np.sin(a))

#print(a<35)

A = np.array([[1, 1],
             [0, 1]])

B = np.array([[2, 0],
             [3, 4]])

#print(A * B) # elementwise product


#print(A.dot(B))# matrix product


#print(np.dot(A, B)) # matrix product

A += B # replace A by A+B only if they are same types

#print(A)

#print(a.sum())

#print(a.max())

#print(a.min())

d = np.array([[ 0, 1, 2, 3  ],
              [ 4, 5, 6, 7  ],
              [ 8, 9, 10, 11]])

#print(d.sum(axis=0)) # asix0 means X and axis1 means Y

#print(d.min(axis=1))

print(d.cumsum(axis=1)) # cumulative sum
