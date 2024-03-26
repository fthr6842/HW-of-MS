import yfinance as yf
from matplotlib import pyplot as plt
import statistics
import pandas as pd
def x_k(a, b): return (a-b)/b
n0 = yf.download('2330.tw', '2021-01-01', '2021-12-31')
n0 = n0['Close'].values.tolist()
c = len(n0)
n1 = [(n0[i+1]-n0[i])/n0[i] for i in range(0, c-1)]
#plt.plot([i for i in range(0, c-1)], n1)#(i)
#plt.hist(n1)#(ii)
plt.show()
#print(max(n1), min(n1), statistics.median(n1))#(iii)
n1 = pd.DataFrame({'return':n1})
#print(n1.describe())#(iv)
#print('SR: ', (0.000678-0.01)/0.014837)#(v)
