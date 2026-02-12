#for joining an array we use concentration keyword

#joining array diffrent array 1d
import numpy as np
arr_1=np.array([1,24,23,24,24,345])
arr_2=np.array([45,463422,534,3,3])
arr_3=np.concatenate((arr_1,arr_2),axis=0)
print(arr_3)

#stack funton
#for stack function all the array shap must be same
arr_5=np.array([1,2,4,5])
arr_6=np.array([3,6,7,4])
arr_4=np.stack((arr_5,arr_6),axis=1)
print(arr_4)