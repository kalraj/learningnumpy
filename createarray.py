a=[1,2,3,4,5]
print(a,id(a[1]))
print(a,id(a[2]))
import numpy as np
b=np.array([1,2,3,4])
print(b,id(b[1]))
print(b,id(b[2]))
# we can also pass a list ,tuple or any array like object with array() and it will be converted to ndarray
c=np.array((1,2,3,4,4,5))
print(c)
print(type(c))
d=np.array({1,2,3,4,4})
print(d)
print(type(d))
print(d.ndim)
#dimension i array -a dimension in arrays is one level of array depth(nested array)
# 0-D arrays - scalers, are the elements in an array, each value in array is a 0-D array
# now we will create 0_d array value 56
e=np.array(56)
print(e)
print(type(e),e.ndim)

# 1-d array- an array that has 0-d arrays as its element is called uni-directional or 1-d
f=np.array([1,2,3,4,5])
print(f,f.ndim)
#creating a 2-=d array containing 2 arrays with certain values
g=np.array([[1,2,3,4],[4,5,6,7]])
print(g,g.ndim)

#now we will create a 3-d array with two 2-d array
h=np.array([[[1,2,9],[4,5,6],[7,8,9],[10,11,12]]])
print(h,h.ndim)
i=np.array([[[[1,2],[4,5],[6,7]]]])
print(i,i.ndim)