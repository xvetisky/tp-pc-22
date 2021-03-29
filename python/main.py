from scipy.optimize import curve_fit
import numpy as np 
from utils import exctract_data
import matplotlib.pyplot as plt 


path_data_libre = "/Users/mac/documents/prepa/rabelais/physique/TPs/tp-pc-22/data-libre/data-y.txt"
path_data_force = "/Users/mac/documents/prepa/rabelais/physique/TPs/tp-pc-22/data-force/data-y.txt"


def function(x, a, b, c):
    return a*np.cos(b*x+c)


def fp(x, a, b, c):
    return -a*b*np.sin(b*x+c)


def ep(x, a, b, c):
    return 1/2*6.6*(function(x, a, b, c)**2)


def ec(x, a, b, c):
    return 1/2*0.0666*(fp(x, a, b, c)**2)


if __name__ == "__main__":
    """
    Cas régime forcé
    """
    file = open(path_data_force, 'r')
    x_data, y_data = exctract_data(file)
    xdata, ydata = np.array(x_data), np.array(y_data)
    popt, pcov = curve_fit(function, xdata, ydata)
    Ec = ec(xdata, *popt)
    Ep = ep(xdata, *popt)
    Em = Ep+Ec
    fig = plt.figure(1, figsize=(10, 6), dpi=80)
    ax1 = fig.add_subplot(211)
    ax1.plot(Ec, 'r-', label='Énergie cinétique')
    ax1.plot(Ep, 'b-', label='Énergie potentielle')
    ax1.plot(Em, 'g', label='Énergie mécanique')
    plt.legend()
    plt.xlabel('temps (s)')
    plt.ylabel('Énergie (J)')
    ax2 = fig.add_subplot(212)
    ax2.plot(function(xdata, *popt), fp(xdata, *popt), '-b', label='Portrait de phase')
    plt.xlabel('Position (m)')
    plt.ylabel('Vitesse (m/s)')
    plt.legend()
    plt.show()
