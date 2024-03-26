#mean=0, standard deviation=1
#f(x)=(1/(1*2*math.pi)**(1/2))*(exp**((-1/2)*((i-0)/1)))
import math
from matplotlib import pyplot as plt
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xticks([0.1*i for i in range(-30, 31, 3)])
plt.yticks([0.1*i for i in range(0, 21)])
plt.plot([0.01*i for i in range(-300, 301)], [(1/(1*2*math.pi)**(1/2))*(math.exp(((-1/2)*((0.01*i-0)/1)))) for i in range(-300, 301)])
plt.grid()
plt.show()
