import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as rnd


# --------------- Multinomial Distribution ------------

x = rnd.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print('Multinomial distribution \n', x)

sns.distplot(x)

plt.show()