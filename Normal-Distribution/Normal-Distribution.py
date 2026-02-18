#normal distrubution is the most important distribution , its the continuos probalility 
#
#Symmetric
#Bell-shaped
#Centered around the mean (μ)
#it have three parameters
#It has three parameters:

#loc - (Mean) where the peak of the bell exists.

#scale - (Standard Deviation) how flat the graph distribution should be.

#size - The shape of the returned ar
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
import seaborn as sns 

arr=np.array([1234,2341,23,123])
sns.displot(arr)
plt.show()
Normal_value=random.normal(size=(3,5))
print(Normal_value)
sns.displot(Normal_value,kind="kde")
plt.show()
sns.displot(Normal_value)
plt.show()
y=random.normal(loc=3,scale=43,size=(4,3))
print(y)
sns.displot(y)
plt.show()