import numpy as np
import matplotlib.pyplot as plt
list0 = [np.random.lognormal(mean=0.0, sigma=0.5) for i in range(100)]
plt.scatter([i for i in range(1, 101)], list0, c='blue')
plt.plot([i for i in range(1, 101)], [sum(list0)/len(list0) for i in range(1, 101)], c='red')
list1 = []
for i in range(0, len(list0)):
    x = sum(list0[:i+1])/len(list0[:i+1])
    list1.append(x)
plt.plot([i for i in range(1, 101)], list1, c='green')
plt.show()