import matplotlib.pyplot as plt

x = [0, 1]
y = [0, 1]

for iter in range(15):
    newY = []
    for i in range(len(y) - 1):
        newY.append(y[i])
        newY.append(y[i] + y[i + 1])
        x.append(x[-1] + 1)
    newY.append(1)
    y = newY

plt.scatter(x, y, s=0.5)
plt.xlabel('n')
plt.ylabel('A002487(n)')
plt.title("A002487 - Suite diatomique de Stern")
plt.show()
