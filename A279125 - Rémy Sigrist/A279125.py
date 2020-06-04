import matplotlib.pyplot as plt

y = []


def smallest_missing_value_in(lst):
    for x in range(min(lst), max(lst) + 2):
        if x not in lst:
            return x


for n in range(1, 10 ** 3):
    if n & (n - 1) != 0:  # if n is not a power of two
        taken_values = []
        for i in range(len(y)):
            if n & (i + 1) != 0:
                taken_values.append(y[i])
        y.append(smallest_missing_value_in(list(dict.fromkeys(taken_values))))
    else:
        y.append(0)

x = range(1, len(y) + 1)
plt.scatter(x, y, s=1)
plt.xlabel('n')
plt.ylabel('A279125(n)')
plt.title("A279125 - Rémy Sigrist")
plt.show()
