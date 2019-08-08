import  numpy as np

data = """
# Skip me !
# Skip me too !
1, 2
3, 4
5, 6 #This is the third line of the data
7, 8
# And here comes the last line
9, 0
"""

print(np.genfromtxt(StringIO(data), comments="#", delimiter=","))
