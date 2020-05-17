# Code by Indranil Ghosh (https://oeis.org/wiki/User:Indranil_Ghosh)

import matplotlib.pyplot as plt


def a(n):
    if n == 0:
        return 0
    if n % 3 == 0:
        return 3 * a(n / 3)
    elif n % 3 == 1:
        return 3 * a((n - 1) / 3) + 1
    else:
        return 3 * a((n - 2) / 3) - 1


y = []
for i in range(100000):
    y.append(a(i))

x = range(len(y))
plt.scatter(x, y, s=0.1)
plt.xlabel('n')
plt.ylabel('A117966(n)')
plt.title("A117966 - Balanced Ternary")
plt.show()
