import numpy as np

a = np.array([[1.0, 2.0],
              [3.0, 4.0]])

#print(a)

#print(np.linalg.inv(a))

u = np.eye(2) # unit 2x2 matrix; "eye" represents "I"

print(u)

j = np.array([[0.0, -1.0],
              [1.0, 0.0]])

#print(np.dot(j, j))

#print(np.trace(u)) #trace

y = np.array([[5.],
              [7.]])

### MATRIX NORMS
#print(np.linalg.norms(a))
#print(np.linalg.conf(a))
#print(np.linalg.det(a))
#print(np.linalg.matrix_rank(a))
#print(np.trace(a))  # sum of diagonal elements

#print(a.transprose())  # Transpose
#same
#print(a.T)  

