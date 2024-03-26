import random as ra
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
z = []
for i in range(0, 1000):
    xn = [ra.gauss(mu=0, sigma=1) for i in range(100)]
    zn = 10*((sum(xn)/len(xn))-0)/1
    z.append(zn)
plt.hist(z)
x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
plt.plot(x, norm.pdf(x)*600, c='red')
plt.show()
