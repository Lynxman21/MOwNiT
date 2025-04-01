from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(1 + 25*x**2)

def create_nodes(node):
    arr = []
    step = 2.0/(node-1)
    current_val = -1.0

    for i in range(node-1):
        arr.append(current_val)
        current_val += step
    
    arr.append(1.0)
    return arr

if __name__ == "__main__":
    n = [i for i in range(2,11)]

    for node in n:
        x = create_nodes(node)
        val_nodes = [f(element) for element in x]
        y = lagrange(x,val_nodes)

        x_plot = np.linspace(-1, 1, 500)
        plt.plot(x_plot, f(x_plot), label="Funkcja oryginalna")
        plt.plot(x_plot, y(x_plot), label="Interpolacja Lagrange’a")
        plt.legend()
        plt.grid()
        plt.show()