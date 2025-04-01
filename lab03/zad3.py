import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline



if __name__ == "__main__":
    #data
    x = input("Enter two edges for interval (with spaces): ").split()
    y = input("Enter three values of your function (with spaces): ").split()
    x = list(map(float,x))
    y = list(map(float,y))
    x1 = (x[1] + x[0]) / 2
    x.insert(1, x1)

    #interpolate
    cub_sp = CubicSpline(x,y)
    x_inter = np.linspace(min(x),max(x),100)
    y_inter = cub_sp(x_inter)

    #plot
    plt.plot(x_inter,y_inter)
    plt.title("Interpolated function")
    plt.scatter(x,y)
    plt.grid()
    plt.show()