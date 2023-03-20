#shape of an array-the shape of an array is the number of elements in each dimensions
#now we will try to get the shape of any array
import numpy as np
a=np.array([1,2,3,4,45,65])
print(a.shape)
b=np.array([[1,2,3],[14,5,6]])
print(b.shape)
c=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(c.shape)
#reshapping=means changing the shape of an array,like adding or removing the element
#reshapping from 1-d to 2-d
kalraj=np.array([1,2,3,4,5,6,7,8,9])
raj=kalraj.reshape(3,3)
print(raj)
kalraj=np.array([1,2,3,4,5,6,7,8])

kal=kalraj.reshape(2,2,2)
print(kal)
kalraj=np.array([1,2,3,4,5,6,7,8,9])
# return copy or view
pal=kalraj.reshape(3,1,3).base
print(pal)

#unknown dimension- you are only allowed to have one unknown dimension pass -1
kalraj=np.array([1,2,3,4,4,5,67,7])
kal=kalraj.reshape(2,2,-1)
print(kal)
#flattening the array by converting multidimensional array in 1-d

kalraj=np.array([[1,2,3],[4,5,6]])
kal=kalraj.reshape(-1)
print(kal)

#there are lot of function for changing the shape of array in numpy. like flattten,ravel and also
#rearranging the element rot90,flip,fliplr,flipud,they all are actually comes under advance numpy
