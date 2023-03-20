# array indexing is the same as accessing an array element
import numpy as np
kalraj=np.array([1,2,3,4])
print(kalraj[0])
print(kalraj[-1])
 
# we can get the third and forth elements from adding them
kalraj=np.array([1,2,3,4,5])
print(kalraj[2]+kalraj[3])

#accessing the 2-d array-it is like a rows and columns
kalraj=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('2nd element of first row ')
print(kalraj[0][1])
print(kalraj[0,1])
print('2nd element of second row ')
print(kalraj[1,1])

# accessig the 3-d array- it is same as accessing 2-d
kalraj=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print('second elemnet of second row')
print(kalraj[0][1][1])
print(kalraj[0,1,1])