import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as rnd


# --------------- Pareto Distribution ------------

x = rnd.pareto(a=2, size=(2, 3))

print('Pareto distribution \n', x)

sns.distplot(rnd.pareto(a=2, size=100))

plt.show()