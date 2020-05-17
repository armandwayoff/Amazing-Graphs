import matplotlib.pyplot as plt

y = [0, 1]

for n in range(15):
    newY = []
    for i in range(len(y) - 1):
        newY.extend((y[i], y[i] + y[i + 1]))
    newY.append(1)
    y = newY

x = range(len(y))
plt.scatter(x, y, s=0.5)
plt.xlabel('n')
plt.ylabel('A002487(n)')
plt.title("A002487 - Stern's Sequence")
plt.show()
