import random, math
def z(): return random.gauss(mu=0, sigma=1)
def y(a, b, z): return a*z+b
def x(y): return math.exp(y)
sigma_squared, mu=0.5, 5
K=110
N=252
list_z=[z() for i in range(0, 252)]
print("(i) list_z", list_z)
list_y=[y(sigma_squared, mu, list_z[i]) for i in range(0, len(list_z))]
print("(ii) list_y", list_y)
list_x=[x(list_y[i]) for i in range(0, len(list_y))]
print("(iii) list_x", list_x)
c=(1/len(list_x))*sum([max(0, list_x[i]-K) for i in range(0, len(list_x))])
print("c=", c)
