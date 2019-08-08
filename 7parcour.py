import numpy as np

a = np.arange(10)**3 # au cube
"""
print(a)

print(a[2])

print(a[2:4])

for i in a:
    print(i**(1/3.)) # just one dimensional arrays
"""

# for multidimensional arrays axis0 an 1(i,j)
#sequencement
def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)
#print(b)
#print(b[2, 3]) # ligne 2 colonne 3

#print(b[0:5, 1]) # les cinq elements en termes de ligne de la colonne 2
#print(b[:, 1]) # meme chose auen haut

#print(b[-1]) # derniere ligne de mme que b[-1, :]


#iteraring
for row in b:
    print(row)

for element in b.flat:
    print(element)
