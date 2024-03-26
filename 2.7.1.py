#problem 2.7.1
#F(x)=x/2, for 0<=x<1；F(x)=1, for x=1
from matplotlib import pyplot as plt
plt.xlabel('x')
plt.ylabel('F(x)')
plt.xticks([0.1*i for i in range(0, 11)])
plt.yticks([0.1*i for i in range(0, 11)])
plt.plot([0.01*i for i in range(0, 100)], [(0.01*i)/2 for i in range(0, 100)], 'g', [1], [1], 'g', marker='.')
plt.grid()
plt.show()
