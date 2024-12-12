import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as rnd


# --------------- Rayleigh Distribution ------------

x = rnd.rayleigh(scale=2, size=(2, 3))

print('Rayleigh distribution \n', x)

sns.distplot(rnd.rayleigh(size=100))

plt.show()