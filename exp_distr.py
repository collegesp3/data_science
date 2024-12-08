import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as rnd


# --------------- Exponential Distribution ------------

x = rnd.exponential(scale=2, size=(2, 3))

print('Exponential distribution \n', x)

sns.distplot(rnd.exponential(size=100))

plt.show()