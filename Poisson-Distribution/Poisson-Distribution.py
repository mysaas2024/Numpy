#poission distrubution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed 
import numpy as np
import seaborn as sns
from numpy import random
import matplotlib.pyplot as plt

x=random.poisson(lam=100, size=(5))
print(x)
sns.displot(x, kind="kde")
plt.show()
sns.displot(x)
plt.show()
sns.displot(random.poisson(lam=1000, size=2))
plt.show()
sns.displot(random.poisson(lam=34, size=(3)))
plt.show()
data={
    "normal":random.normal(loc=34,scale=3,size=4),
    "binomail":random.binomial(n=23, p=0.4, size=4),
    "poisson":random.poisson(lam=34,size=4 )
}
sns.displot(data)
plt.show()
sns.displot(data,kind="kde")
plt.show()

