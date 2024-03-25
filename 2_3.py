import yfinance as yf
df = yf.download("2330.tw", start="2022-01-01", end="2022-12-31")
list0 = ((df["Close"].shift(1) - df["Close"])/df["Close"]).to_list()[1:]
def f0(x): return sum(x)/len(x)
def f1(x):
    k = 1
    for i in x: k *= (1+i)
    return k**(1/len(x))-1
def f2(x): return len(x)*(1/sum([(1/1+i) for i in x]))-1
if __name__ == "__main__":
    print("arithmic mean: ", f0(list0))
    print("geometric mean: ", f1(list0))
    print("harmonic mean: ", f2(list0))
