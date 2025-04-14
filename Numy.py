#create numpy array
import numpy as np 
array1 = np.array([1,2,3,4,5])
print(array1)
#properties of numpy array
print(array1.ndim)
array2 = np.array([[1,2,3,4,5],[0,9,8,7,6]])
print(array2)
#properties of numpy array
print(array2.ndim)
array5 = np.array([[[[[1,2,3,4,5]],[[5,7,9,3,1]]]]]) # 5 dimensional array [[[[[]]]]]
print(array5)
#properties of numpy array
print(array5.ndim)
#Numpy function
print(array1.shape) #shape
print(array1.ndim) #dimensiom
print(array1.size) #noofelements
print(array1.dtype) #datatype
print(array1.argmax())
print(array2)
print(array2.argmin(axis = 0))
print(array2.argmin(axis = 1))
print(array2.argmax(axis = 0))
print(np.argmax(array2,axis = 1))
print(array2[1,1])
a = np.arange(6).reshape(2,3) + 10
print("array a:",a)
#np.argmax(a)
print(np.argmax(a))
np.argmax(a, axis=0)
print(np.argmax(a))
np.argmax(a, axis=1)
print(np.argmax(a))
print(a[1,2])
print()