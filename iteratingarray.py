# iterating array - means going through the elements one by one or step by step.like for loop

#iterating the element of 1-d
import numpy as np
kalraj=np.array([1,2,3,4,5])
for i in kalraj:
    print(i,end=' ')
print()
#iterate 2-d
kalraj=np.array([[1,2,3],[4,6,7]])
for i in kalraj:
    print(i)

#iterate each scalar element of the 2-d
kalraj=np.array([[1,2,3],[4,5,6]])
for i in kalraj:
    for k in i:
        print(k,end='')
print()
#iterating array using the nditer() function
#now we will iterate on each scaler element
kalraj=np.array([[[[1,2,3,4,5],[6,7,8,9,0]]]])
for i in np.nditer(kalraj):
    print(i ,end='')
    