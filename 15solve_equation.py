import numpy as numpy

A = np.array([[1.0, 2.0],
              [3.0, 4.0]])

a = np.full((4, 5), 10)

b = np.random.random((3, 1))

# if matrix is not invertable like A use the sudo inverse matrix
x0 = np.linalg.pinv(A)

x1 = np.matmul(np.linalg.inv(a), b) # inverse of A time b
# samething with solve function
x2 = np.linalg.solve(A, B)

#operations
print(np.multiply(a,b), dtype = np.float128)
print(np.divide(a,b), dtype=np.int64)

#matrix operations
print(np.matmul(a,b)) # error if multipl with non compatible dimensions
#same
print(np.dot(a,b))
#same
print(np.inner(a,b))







