#shuffling of arrays
#the shufflu methiode chandges the origanal array.
import numpy as np
from numpy import random

arr=np.array([1,234,3432,33])
random.shuffle(arr)
print(arr)

#the permutation methode nt changes the orignal arr
arr_1=np.array([23,3343,23])
print(arr_1)
#making it random
print(random.permutation(arr_1))