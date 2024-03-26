#mean=0, standard deviation=1
#f(x)=(1/(1*2*math.pi)**(1/2))*(math.exp**((-1/2)*((math.log(i)-0)/1)))*abs(1/i)
import math
from matplotlib import pyplot as plt
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xticks([0.1*i for i in range(0, 61, 6)])
plt.yticks([i for i in range(0, 101)])
plt.plot([0.01*i for i in range(1, 601)], [(1/(1*2*math.pi)**(1/2))*(math.exp(((-1/2)*((math.log(0.01*i)-0)/1))))*abs(1/i) for i in range(1, 601)])
plt.grid()
plt.show()
