import numpy as np
a=np.array([1,2,3,4,5,7])
print(type(a))
print(a.ndim)
print(a.astype('S'))
b=np.array([1,2,3,4,5,7],dtype='i')
print(b)
print(type(b))
print(b.astype('O'))
print(type(b))