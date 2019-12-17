import numpy as np
import matplotlib.pyplot as plt

l = np.pi
x_range = np.arange(-l, l, 0.1)

a0 = 1 / 2


def an(n):
    return 0


def bn(n):
    return (1 - np.cos(n * np.pi)) / (n * np.pi)


def f(x):
    r = a0

    for n in range(1, 1000):
        r += an(n) * np.cos((n * x * np.pi) / l) + bn(n) * np.sin((n * x * np.pi) / l)

    return r


plt.plot(x_range, f(x_range).astype(np.float))
plt.show()
