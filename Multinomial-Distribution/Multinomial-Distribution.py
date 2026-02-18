import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x=random.multinomial(n=3, pvals=[1/6, 2/6 ,2/6] ,size=(6))
print(x)
plt.plot(x)
plt.show()
