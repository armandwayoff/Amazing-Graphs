import matplotlib.pyplot as plt
from math import gcd

y = [1, 1]

for n in range(2, 10 ** 3):
    if gcd(n, y[n - 1]) == 1:
        y.append(y[n - 1] + n + 1)
    else:
        y.append(int(y[n - 1] / gcd(n, y[n-1])))

x = range(len(y))
plt.figure("A133058 - Fly straight, dammit")
plt.scatter(x, y, s=8)
plt.xlabel('n')
plt.ylabel('A133058(n)')
plt.title("A133058 - Fly straight, dammit")
plt.show()
