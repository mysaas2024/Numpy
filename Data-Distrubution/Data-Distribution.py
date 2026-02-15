#data distribution 
from numpy import random
arr=random.choice([1234,23343,32],p=[0.2,0.5,0.3], size=(3,5))
print(arr)