import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
#np.where is a function where it find the simlar number it  return its index number



arr_1=np.array([24,434343,43,534,3,43,3])
arr_2=np.where(arr_1%2==0)
print(arr_2)



#search sort is a also a funtion which does the job but keep the array cleaan 
arr_4 = np.array([10, 20, 30, 40, 50])

# Where should 35 go to keep array sorted?
index = np.searchsorted(arr_4, 35)
print(index)
