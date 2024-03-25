import matplotlib.pyplot as plt
s0, s1 = [(2*i-1)/i**2 for i in range(1, 101)], [2/(i-1) for i in range(2, 101)]
plt.plot([i for i in range(1, 101)], s0, c="red")
plt.plot([i for i in range(2, 101)], s1, c="black")
plt.show()
