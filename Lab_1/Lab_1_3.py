import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 1, 0.01)
x = np.arange(0, 4, 0.01)
f_1 = lambda x:  (np.power(np.e, -x)) * (x >= 0)
f_2 = lambda x: -(np.power(np.e, -x)) * (x >= 0)
f_3 = lambda x: (np.log(1 - x)) * (x >= 0)


y1 = f_1(x)
y2 = f_2(x)
y3 = f_3(y)


plt.figure(1)
plt.plot(x, y1)
plt.title("Gestosc prawdopodobienstwa")
plt.xlabel('X')
plt.ylabel('f(x)')

plt.figure(2)
plt.plot(x, y2)
plt.title("Wykres dystrybuanty")
plt.xlabel('F(x)')
plt.ylabel('x')

plt.figure(3)
plt.plot(y, y3)
plt.title("Wykres odwrotnej dystrybuanty")
plt.xlabel('y(x)')
plt.ylabel('x')

plt.figure(4)
plt.hist(y3 , density=True)
plt.plot(x,y1)
plt.title("histogram odwrotnej dystrybuanty")
plt.xlabel('wartosc probki')
plt.ylabel('Ilosc probek')



plt.show()





plt.show()
