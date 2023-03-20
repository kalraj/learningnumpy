#slicing array-slicing in python means taking element from one given index to another index
#[start:end],[start:end:step]
import numpy as np
kalraj=np.array([1,2,3,4,5,6,7,8])
print(kalraj[1:5])

#now we will slice from index 4 to the end value
kalraj=np.array([1,2,3,4,5,6,7,8])
print(kalraj[4:])

# ow we will slice the element from the begining to index 4
kalraj=np.array([1,2,3,4,5,6,7,8])
print(kalraj[:4])

#negative indexing
kalraj=np.array([1,2,3,4,5,6,7,8])
print(kalraj[-1])

# by using negative indexing 3 to end
kalraj=np.array([1,2,3,4,5,6,7,8])
print(kalraj[-6:-1])

#slicing 2-d array
kalraj=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(kalraj[1][1:4])
print(kalraj[1,1:4])
print(kalraj[0,1:4])
print(kalraj[0,-3:-1])
