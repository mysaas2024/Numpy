import numpy as np
#copy thing in python
arr = np.array([1,35,22,434,24,34,2])
copy_arr=arr.copy()
print(copy_arr)
#changing things in the copy Array
arr[4]=34
copy_arr[0]=33
#printing the origanl array
print(arr)
#printing thr copy arr
print(copy_arr)

#View
arr_1=np.array([24,235,32523,22])
#origanl array
print(arr_1)
arr_view=arr_1.view()
#view thing 
print(arr_view)
#changing thing in the view
arr_view[1]=2334
print(arr_view)