import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x=random.binomial(n=10,p=0.5, size=(3,5))
print(x)
sns.displot(x)
plt.show()
sns.displot(x, kind="kde")
plt.show()
sns.displot(x, kind="ecdf")
plt.show()
sns.displot(x,kind="hist")
plt.show()
sns.displot(random.binomial(n=10, p=0.5, size=1000))
plt.show()

data={
    "normal":random.normal(loc=23,scale=34,size=4),
    "binomal":random.binomial(n=23,p=0.3,size=4)

}
sns.displot(data,kind="kde")
plt.show()

