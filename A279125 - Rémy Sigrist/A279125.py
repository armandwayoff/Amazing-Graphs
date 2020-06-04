import matplotlib.pyplot as plt

y = [0]


def find_missing(lst):
    lt = [x for x in range(lst[0], lst[-1] + 1)
          if x not in lst]
    if len(lt) > 0:
        return min(lt)
    else:
        return max(lst) + 1


for n in range(2, 1000):
    if n & (n - 1) != 0:
        delete = []
        for i in range(len(y)):
            if n & (i + 1) != 0:
                delete.append(y[i])
        delete = list(dict.fromkeys(delete))
        y.append(find_missing(delete))
    else:
        y.append(0)

x = range(1, len(y) + 1)
plt.scatter(x, y, s=1)
plt.xlabel('n')
plt.ylabel('A279125(n)')
plt.title("A279125 - Rémy Sigrist")
plt.show()
