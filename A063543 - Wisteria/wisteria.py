import matplotlib.pyplot as plt

x = []
y = []

for i in range(1, 2000):
    chiffres = map(int, str(i))
    produit = 1
    for c in chiffres:
        if c != 0:
            produit *= c
    x.append(i)
    y.append(i - produit)

plt.scatter(x, y, s=0.3)
plt.xlabel('n')
plt.ylabel('A063543(n)')
plt.title("A063543 - Wisteria")
plt.show()
