import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as rnd

""" sns.distplot([0, 1, 2, 3, 4, 5])

plt.show() """

# --------------- Normal Distribution ------------

x = rnd.normal(size=(2, 3))

print('Normal distribution of size 2x3 \n', x)

x = rnd.normal(loc=1, scale=2, size=(2, 3))

print('Normal distribution of size 2x3 with mean at 1 and standard deviation of 2 \n', x)

sns.distplot(rnd.normal(size=1000), hist=False)

plt.show()
