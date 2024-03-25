import random as ra
import matplotlib.pyplot as plt
import statistics as stat
#Let a:=0.7
a=0.5
#Let mu:=0
mu=0
#Let size of sample set be 100
n=100
#Given that x is a list with its length>=2
def Var(x):
    return stat.variance(x)
#sample set
sample=[]
for i in range(1,n+1):
    sample.append(ra.gauss(mu=mu,sigma=1))
#variance set of estimator
Sita=[]
Sita_New=[]
count=[]
for i in range(1,n):
    Sita.append(Var(sample[0:i+1])/(i+1))
    Sita_New.append(((a**2/i+1)+(1-a)**2)*Var(sample[0:i+1]))
    count.append(i)
plt.plot(count,Sita,c='blue')
plt.plot(count,Sita_New,c="green")
plt.show()
