import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as rnd

# ----------- Poisson Distribution --------------

xPoi = rnd.poisson(lam=2, size=100)
xNorm = rnd.normal(loc=2, scale=1, size=100)
xBin = rnd.binomial(n=100, p=0.02, size=100)

print(xPoi)

#sns.distplot(x, kde=False)

sns.distplot(xNorm, hist=False, label='normal')
sns.distplot(xBin, hist=False, label='binomial')
sns.distplot(xPoi, label='poisson')


plt.show()