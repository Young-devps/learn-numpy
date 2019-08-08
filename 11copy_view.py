import  numpy as np

a = np.arange(12)
b = a
# no new object is created
print(b is a)
# a and b are two names for the same ndarray object
b.shape = 3,4
# changes the shape of a

print(a.shape)

c = a.view()
print(c is a)

print(c.base is a) # c is a view of the data owned by a

print(c.flags.owndata)

c.shape = 2,6 # a's shape doesn't change
print(a.shape)

c[0,4] = 1234 # a's data changes
print(a)


d = a.copy() # a new array object with new data is created
print(d is a)

print(d.base is a) # d doesn't

d[0,0] = 9999
print(a)

