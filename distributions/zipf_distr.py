import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as rnd


# --------------- Zipf Distribution ------------

x = rnd.zipf(a=2, size=(2, 3))

print('Zipf distribution \n', x)

x = rnd.zipf(a=2, size=1000)

sns.distplot(x[x<10])

plt.show()