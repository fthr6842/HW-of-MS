import numpy
from statistics import variance, mean
def f0(n=20, p=0.6, size=10): return numpy.random.binomial(n, p, size)
def sita(n, xi): return mean(xi)/(1-variance(xi)/mean(xi)), 1-variance(xi)/mean(xi)
if __name__ == "__main__":
    n0, n1, n2 = f0(), f0(size=100), f0(size=1000)
    print("results of (i): ", sita(len(n0), n0))
    print("results of (ii): ", sita(len(n1), n1), sita(len(n2), n2))

