import random
from matplotlib import pyplot as plt
list0, list1=[], []
for i in range(0, 1000):
    list0.append(random.gauss(mu=0, sigma=1)+random.gauss(mu=1, sigma=1))#u
    list1.append(random.gauss(mu=0, sigma=1)-random.gauss(mu=1, sigma=1))#v
plt.hist(list0, bins=100)
plt.hist(list1, bins=100)
plt.show()
print(sum(list0)/len(list0), )#1.0011409063880996
print(sum(list1)/len(list1))#-0.9359703955446476
import numpy as np
print(np.var(list0))#1.987593863898648
print(np.var(list1))#1.9690695928422919
