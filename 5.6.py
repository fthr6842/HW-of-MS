from matplotlib import pyplot as plt
import math
plt.xlabel('x')
plt.ylabel('value')
plt.bar([i for i in range(0, 11)], [(math.exp(-(12)**(1/2))*((12)**(1/2))**i)/math.factorial(i) for i in range(0, 11)])
plt.show()

