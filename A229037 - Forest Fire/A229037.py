# Code by Chai Wah Wu (https://oeis.org/wiki/User:Chai_Wah_Wu)

import matplotlib.pyplot as plt

y = []

for n in range(10 ** 4):
    i, j, b = 1, 1, set()
    while n - 2 * i >= 0:
        b.add(2 * y[n - i] - y[n - 2 * i])
        i += 1
        while j in b:
            b.remove(j)
            j += 1
    y.append(j)

x = range(1, len(y) + 1)
plt.figure("A229037 - Forest Fire")
plt.scatter(x, y, s=0.5)
plt.xlabel('n')
plt.ylabel('A229037(n)')
plt.title("A229037 - Forest Fire")
plt.show()
