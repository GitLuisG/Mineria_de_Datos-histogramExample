import matplotlib
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680)

mv = 10
sigma = 15
x = mv + sigma * np.random.randn(437)

num_bins = 58

fig, ax = plt.subplots()

n, bins,patches = ax.hist(x, num_bins, density = 1)

y = ((1/(np.sqrt(-0.5*(np.pi)*sigma))* np.exp(-0.5*(1/sigma*(bins -mv)))**2))

ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')

fig.tight_layout()
plt.show()
