import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x=random.uniform(size=10)
print(x)
sns.displot(x)
plt.show()
sns.displot(x , kind="kde")
plt.show()
data = random.uniform(0, 1, 1000)

plt.hist(data, bins=20)
plt.title("Uniform Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()