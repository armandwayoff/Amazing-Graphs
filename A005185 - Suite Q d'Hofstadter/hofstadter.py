import matplotlib.pyplot as plt

x = [1, 2]
y = [1, 1]

for i in range(2, 10000):
    x.append(i + 1)
    y.append(y[i - y[i - 1]] + y[i - y[i - 2]])

plt.scatter(x, y, s=0.1)
plt.xlabel('n')
plt.ylabel('A005185(n)')
plt.title("A005185 - Suite Q d'Hofstadter")
plt.show()
