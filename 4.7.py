import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
n0=yf.download('2330.tw', start='2020-01-01', end='2021-01-01')
n0=n0.iloc[:, 4]
n1=(n0.shift(1)-n0)/n0
print("sample mean of returns", n1.mean())
n1=n1.dropna()
n2=n1.to_list()
n3=[(i-n1.mean())**2 for i in n2]
print("sample variance of returns", (1/(len(n1.to_list())-1))*sum(n3))
plt.plot(n0.index.to_list(), n0.to_list())
plt.title('2330.tw')
plt.xlabel('time')
plt.ylabel('price')
plt.show()
