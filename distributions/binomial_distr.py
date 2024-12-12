import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as rnd

# ---------- Binomial Distribution ---------

xBin = rnd.binomial(n=100, p=0.5, size=100)
xNorm = rnd.normal(loc=50, scale=5, size=100)

#print(xBin)

#sns.distplot(rnd.binomial(n=10, p=0.5, size=100), hist=True, kde=False)

sns.distplot(xBin, hist=False, label='binomial')
sns.distplot(xNorm, hist=False, label='normal' )

plt.show()