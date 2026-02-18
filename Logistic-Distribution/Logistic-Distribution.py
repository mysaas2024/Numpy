import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.logistic(size=1000),kind="kde")
plt.show()
x=np.array(random.normal(loc=23, scale=0.4 ,size=3))
y=np.array(random.normal(loc=23, scale=0.6 ,size=3))
plt.scatter(x,y)
plt.show()
