import math, random
def f0(x): return math.cos(2*math.pi*x)
list0=[10, 100, 1000, 100000]
for i in range(0, len(list0)):
    list1=[]
    for j in range(0, list0[i]): list1.append(f0(random.gauss(mu=0, sigma=1)))
    print("N=", list0[i], ": ", sum(list1)/len(list1))
