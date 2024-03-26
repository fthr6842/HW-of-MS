#2.6.5
#P(X = i) = 1/6, for i = 1, 2, . . . , 6
F_x=[]
for i in range(1, 7):
    if i==1: F_x.append(1/6)
    else: F_x.append(F_x[i-2]+1/6)
from matplotlib import pyplot as plt
plt.xlabel('x')
plt.ylabel('F(x)')
plt.xticks(range(1, 7))
plt.yticks([0.1*i for i in range(0, 11)])
plt.plot([i for i in range(1, 7)], F_x)
plt.grid()
plt.show()
