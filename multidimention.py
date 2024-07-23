import numpy as np

list1=[1,2,3,4]
list2=[3,4,5,6]
list3=[6,7,8,9]

m_numpy = np.array([list1,list2,list3])

print(m_numpy)

print(type(m_numpy))

print(m_numpy.shape)

print(m_numpy.dtype)

#iterate
iterable = (a*a for a in range(8))

arr = np.fromiter(iterable,float)
print(arr)

import numpy as np

print(np.arange(1, 20 , 2, 
          dtype = np.float32))

arr = np.empty([4],dtype= np.int32, order='f')
print(arr)