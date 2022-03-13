import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-0.99, 2, 0.01)
f_1 = lambda x: (x + 1) * (x > -1) * (x < 0) + (-x + 1) * (x >= 0) * (x < 1)
f_2 = lambda x: (0.5 + x + x**2/2) * (x < 0) * (x > -1) + (0.5 + x - x**2/2) * (x >= 0) * (x < 1) + (x >= 1)
f_3 = lambda x: (np.sqrt(x * 2) - 1) * (x >= 0) * (x <= 0.5) + (1 - np.sqrt(2 - x * 2)) * (x > 0.5) * (x <= 1) - (x < -1)

y = f_1(x)
y2 = f_2(x)
y3 = f_3(x)


plt.figure(1)
plt.plot(x, y)
plt.title("Gestosc prawdopodobienstwa")
plt.xlabel('X')
plt.ylabel('f(x)')

plt.figure(2)
plt.plot(x, y2)
plt.title("Wykres dystrybuanty")
plt.xlabel('F(x)')
plt.ylabel('x')

plt.figure(3)
plt.plot(x, y3)
plt.title("Wykres odwrotnej dystrybuanty")
plt.xlabel('y(x)')
plt.ylabel('x')

plt.figure(4)
plt.hist(y3 , density=True)
plt.plot(x, y)
plt.title("histogram odwrotnej dystrybuanty")
plt.xlabel('wartosc probki')
plt.ylabel('Ilosc probek')



plt.show()





plt.show()
