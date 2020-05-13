import matplotlib.pyplot as plt
import math

y = [1, 1]

for n in range(2, 1000):
    if math.gcd(n, y[n - 1]) == 1:
        y.append(y[n - 1] + n + 1)
    else:
        y.append(int(y[n - 1] / math.gcd(n, y[n-1])))

x = range(len(y))
plt.scatter(x, y, s=8)
plt.xlabel('n')
plt.ylabel('A133058(n)')
plt.title("A133058 - Fly Staight Dammit!")
plt.show()
