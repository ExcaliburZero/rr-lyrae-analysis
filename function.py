import math
import matplotlib.pyplot as plt
import numpy as np

mu  = 0.5636773 # Mean
row = 0.1076015 # Standard deviation

def f(x):
    """Population density function for RR Lyrae star periods."""
    return (1 / math.sqrt(2 * (row ** 2) * math.pi)) * (math.e ** (- (((x - mu) ** 2) / (2 * (row ** 2)))))

def g(x):
    """Probability function for RR Lyrae star periods."""
    return f(x) / f(mu)

def main():
    # Generate the (x, y) data
    start = 0.2
    end = 0.9
    interval = 0.005
    xs = [x for x in np.arange(start, end, interval)]
    results = [g(x) for x in xs]

    # Plot the data
    plt.plot(xs, results)

    # Plot standard deviation lines
    for x in range(-3,4):
        plt.axvline(mu + (x * row), color="red")

    # Show the graph
    plt.show()

if __name__ == '__main__':
    main()
