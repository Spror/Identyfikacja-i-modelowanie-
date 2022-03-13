import numpy as np
import matplotlib.pyplot as plt


def sawtooth_generator(seed, start_value, n):
    x_n = start_value
    for i in range(n):
        yield x_n
        x_n = seed*x_n - np.floor(seed*x_n)


z = 33 #seed
X_0 = 0.2  # first value
N = 100000   # number of digits

xN = [i for i in sawtooth_generator(z, X_0, N)]
time = [i for i in range(N)]
y = np.zeros(N)

plt.figure(1)
plt.hist(xN)
plt.title("Z = " + str(z) + ", X = " + str(X_0) + ", N = " + str(N))
plt.xlabel('Wartosc probki')
plt.ylabel('Ilosc probek o danej wartosci')

plt.figure(2)
plt.plot(time, xN, 'bo-')
plt.title("Z = " + str(z) + ", X = " + str(X_0))
plt.xlabel('Numer probki')
plt.ylabel('Wartosc probki')

plt.show()
