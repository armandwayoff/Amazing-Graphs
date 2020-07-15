import matplotlib.pyplot as plt

y = [1, 1]

for i in range(2, 10 ** 4):
    y.append(y[i - y[i - 1]] + y[i - y[i - 2]])

x = range(1, len(y) + 1)
plt.figure("A005185 - Hofstadter's Q Sequence")
plt.scatter(x, y, s=0.1)
plt.xlabel('n')
plt.ylabel('A005185(n)')
plt.title("A005185 - Hofstadter's Q Sequence")
plt.show()
