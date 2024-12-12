import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as rnd


# --------------- Chi Square Distribution ------------

x = rnd.chisquare(df=2, size=(2, 3))

print('Chi Square distribution \n', x)

sns.distplot(rnd.chisquare(df=1, size=100))

plt.show()