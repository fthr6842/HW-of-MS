import random
def f0(): return sum([random.randint(0, 1) for i in range(0, 10)])#隨機生成函數
def f1(k = 4, x=1):#階層函數
    for i in range(x, k+1): x *= i
    return x
#(i)k次上漲機率
def f2(k, n = 10, p = 0.5): return (f1(n)/(f1(k)*(f1(n-k))))*((p)**k)*((1-p)**(n-k))
#(ii)期望值
def f3(n = 10, p = 0.5): return sum([i*f2(i, n, p) for i in range(1, n+1)])
if __name__ == "__main__":
    print(f2(k=7))
    print(f3())
