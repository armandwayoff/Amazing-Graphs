import matplotlib.pyplot as plt
import sympy

x, y = [], []

for i in range(10 ** 5):
    if sympy.isprime(i):
        x.append(i)
        y.append(i - int(bin(i)[:1:-1], 2))

plt.figure("A265326 - Primes")
plt.scatter(x, y, s=0.5)
plt.xlabel('n')
plt.ylabel('A265326(n)')
plt.title("A265326 - Primes")
plt.show()
