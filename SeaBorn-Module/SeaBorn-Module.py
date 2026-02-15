#seaborn is a python library that make a graph of the random distribution
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from numpy import random
sns.displot([0, 1, 2, 3, 4, 5])

plt.show()

arr=random.choice([2424,2324,232,42,32,34],size=(3))
sns.displot(arr)
plt.show()
sns.displot([0, 1, 2, 3, 4, 5], kind="kde")

plt.show()