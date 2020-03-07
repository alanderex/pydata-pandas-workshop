import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1)

x = np.random.normal(5, 2, 10000)
y = np.random.normal(2, 1, 3000000)

xweights = 100 * np.ones_like(x) / x.size
yweights = 100 * np.ones_like(y) / y.size

fig, ax = plt.subplots()
ax.hist(x, weights=xweights, color='lightblue', alpha=0.5, density=True)
ax.hist(y, weights=yweights, color='salmon', alpha=0.5, density=True)

ax.set(title='Histogram Comparison', ylabel='% of Dataset in Bin')
ax.margins(0.05)
ax.set_ylim(bottom=0)
plt.show()