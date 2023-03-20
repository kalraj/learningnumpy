# putting contents of two or more arays in a single array
#by concatenate() function
import numpy as np
arr=np.array([1,2,3,4])
arr1=np.array([5,6,7,8])
arr3=np.concatenate((arr,arr1))
print(arr3)
# joining 2-d array
arr=np.array([[1,2,3],[5,6,7]])
arr1=np.array([[5,6,9],[10,11,12]])
arr3=np.concatenate((arr,arr1))
print(arr3)

#joining array using stack function
arr=np.array([1,2,3])
arr2=np.array([5,6,7])
arr3=np.stack((arr,arr2))
print(arr3)
arr3=np.stack((arr,arr2),axis=1)
print(arr3)

#STACKING along rows by using hstack() function
arr=np.array([1,2,3])
arr2=np.array([5,6,7])
arr3=np.hstack((arr,arr2))
print(arr3)
print(dir(list))
a=[1,56,73,25,95,76]
# a = (1, 5, 3, 9)
# x = max(a)
# b=tuple(a)
print(type(a))
x=max(a)
print(x)
print(a[1:3])
print(a[-1:-3])