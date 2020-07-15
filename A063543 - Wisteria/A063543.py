import matplotlib.pyplot as plt

y = []

for i in range(1, 2000):
    digits = map(int, str(i))
    product = 1
    for d in digits:
        if d != 0:
            product *= d
    y.append(i - product)

x = range(1, len(y) + 1)
plt.figure("A063543 - Wisteria")
plt.scatter(x, y, s=0.3)
plt.xlabel('n')
plt.ylabel('A063543(n)')
plt.title("A063543 - Wisteria")
plt.show()
