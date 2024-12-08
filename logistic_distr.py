import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as rnd


# --------------- Logistic Distribution ------------

x = rnd.logistic(loc=1, scale=2, size=(2, 3))


print('Logistic distribution of size 2x3 \n', x)


sns.distplot(rnd.normal(scale=2, size=100), hist=False, label='normal')
sns.distplot(rnd.logistic(size=100))

plt.show()