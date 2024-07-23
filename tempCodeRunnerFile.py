import numpy as np

print(np.arange(1, 20 , 2, 
          dtype = np.float32))

arr = np.empty([4],dtype= np.int32, order='f')
print(arr)