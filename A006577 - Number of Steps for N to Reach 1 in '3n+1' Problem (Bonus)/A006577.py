import matplotlib.pyplot as plt

y = []

for n in range(1, 10 ** 4):
    count = 0
    while n > 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        count += 1
    y.append(count)

x = range(1, len(y) + 1)
plt.scatter(x, y, s=0.5)
plt.xlabel('n')
plt.ylabel('A006577(n)')
plt.title("A006577 - Number of Steps for N to Reach 1 in '3n+1' Problem (Bonus)")
plt.show()
