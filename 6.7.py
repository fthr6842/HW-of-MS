import random
from matplotlib import pyplot as plt
random.seed(10)
list0=[random.gauss(mu=0.1*0.01, sigma=0.15*0.01) for i in range(0, 252)]#X_k
list1=[1]
for i in range(0, len(list0)): list1.append((1+list0[i])*list1[i])
print('V_k = ',list1)#V_k#(i)
#=================================================
list4=[]
for i in range(0,10):
    list2=[1]
    list3=[random.gauss(mu=0.1*0.01, sigma=0.15*0.01) for i in range(0, 252)]
    for i in range(0, len(list3)): list2.append((1+list3[i])*list2[i])
    list4.append(list2[-1])
    plt.plot([i for i in range(0, len(list2))], list2)
print('average terminal account values over the 10 samples = ', sum(list4)/len(list4))#(iii)
plt.show()#(ii)
