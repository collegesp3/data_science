import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as rnd


# --------------- Uniform Distribution ------------

x = rnd.uniform(size=(2, 3))

print('Uniform distribution of size 2x3 \n', x)

sns.distplot(rnd.uniform(low = -5, high = 2, size=1000))

plt.show()