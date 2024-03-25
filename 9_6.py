import matplotlib.pyplot as plt
from scipy.stats import norm
def f0(x): return 1 - norm.cdf((75-x)/2)
ydata = [f0(i) for i in range(50, 76)]
plt.plot([i for i in range(50, 76)], ydata)
plt.show()
