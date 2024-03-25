import matplotlib.pyplot as plt
x = [0.01*i for i in range(0, 130)]
y1 = [1 for i in range(0, 51)]
y2 = [1/((2*x[i])**4) for i in range(51, 101)]
y3 = [(1-(15/((2*x[i])**4))) for i in range(101, 130)]
y = y1 + y2 + y3
plt.plot(x, y)
plt.show()
