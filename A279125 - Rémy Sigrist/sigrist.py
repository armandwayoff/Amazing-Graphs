import matplotlib.pyplot as plt
import math

y = [0]
valPrises = [[0]]


def decomposition(arr):
    powers = []
    iter = 1
    while iter <= arr:
        if iter & arr:
            powers.append(int(math.log(iter, 2)))
        iter <<= 1
    return powers


def minimumlist(arr):
    a = 0
    for i in range(len(arr)):
        if a < max(arr):
            if a == arr[i]:
                a += 1
            else:
                return a
        else:
            a = max(arr) + 1
            return a


for i in range(2, 1000):
    if len(decomposition(i)) != 1:
        valEliminer = []
        for j in range(len(decomposition(i))):
            valEliminer = valEliminer + valPrises[decomposition(i)[j]]
        valEliminer.sort()
        valEliminer = list(dict.fromkeys(valEliminer))
        y.append(minimumlist(valEliminer))
        for j in range(len(decomposition(i))):
            valPrises[decomposition(i)[j]].append(minimumlist(valEliminer))
    else:
        y.append(0)
        valPrises.append([0])

x = range(1, len(y) + 1)
plt.scatter(x, y, s=1)
plt.xlabel('n')
plt.ylabel('A279125(n)')
plt.title("A279125 - Rémy Sigrist")
plt.show()
