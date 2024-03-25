from statistics import mean, variance
import yfinance as yf
import scipy.stats
data = yf.download("2330.tw", "2022-01-01", "2022-12-31")
x = data["Close"].to_list()
def t(x): return (mean(x) - 0.01)/variance(x)
def pvalue(t, df): return scipy.stats.t.sf(abs(t), df)
if __name__ == "__main__": print(0.5 - pvalue(t(x), len(x)-1))
