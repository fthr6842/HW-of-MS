from scipy.stats import chi2
print("critical values:", chi2(0.05, 10), "\n", chi2(1-0.05, 10))
