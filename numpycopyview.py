#copy and view
#we will make a copy chage in original array but no effect in copy array
import numpy as np
kalraj=np.array([1,2,3,4,5,6])
raj=kalraj.copy()
print(raj)
print(kalraj)
#in copy if we change done it will not effect the original array
raj[1]=3000
print('copy array :',raj)
print('original array :',kalraj)
# view
kalraj=np.array([1,2,3,4,5,6])
raj=kalraj.view()
print('view array :',raj)
print('original array',kalraj)
#in view if any change done it will also effect the the original array
raj[1]=1000
print('copy array :',raj)
print('original array :',kalraj)