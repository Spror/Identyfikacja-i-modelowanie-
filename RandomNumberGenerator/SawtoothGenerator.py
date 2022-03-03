import numpy
import numpy as np
import math
import matplotlib.pyplot as plt
def sawtooth_generator():
    seed = int(input("Enter seed: "))
    digits_amount = int(input("Eneter amount of digits: "))
    frequency  = int(input("Enter a frequency of the sawtooth function: "))

    if seed > 1:
        seed = 1

    if seed < 1:
        seed = 0

    if digits_amount < 1:
        digits_amount = 1

    tmp = seed
    gen_output = np.zeros((1, digits_amount))

    for i in range(0, digits_amount):
        a = 171.1212*tmp
        tmp = a - math.floor(a)
        gen_output[0, i] = tmp

    print(gen_output)
    bins = np.arange(0,1,0.01)
    plt.hist(numpy.transpose(gen_output), bins)
    plt.show()


a = np.arange(15).reshape(3, 5)

print(a)

sawtooth_generator()





