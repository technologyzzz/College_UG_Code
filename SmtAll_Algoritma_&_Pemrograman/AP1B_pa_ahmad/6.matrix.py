"""
m = 10
n = 5
x = [0]*m

for i in range(m):
    x[i] = [1]*n
print(x)    

import array as arr
a = arr.array('i', [1,2,3,4,5])
print(a)

import numpy as np
arr = np.array('i', [1,2,3,4,5])
print(arr)

a = [1,2,3,4,5]
b = ['a', 'b', 'c']
c = 

from numpy import *
matriks = range(12)
matriks = reshape(matriks,(4,3))
print(matriks)
"""

import numpy as np
matriks = np.random.randint(1,4,(3,4))
print(matriks)
