import math
import matplotlib.pyplot as plt
import numpy as np
import sys

mu  = 0.5445663 # Mean
row = 0.1208535 # Standard deviation

def f(x):
    """Population density function for RR Lyrae star periods."""
    return (1 / math.sqrt(2 * (row ** 2) * math.pi)) * (math.e ** (- (((x - mu) ** 2) / (2 * (row ** 2)))))

def g(x):
    """Probability function for RR Lyrae star periods."""
    return f(x) / f(mu)

def main():
    # Determine the graph file type
    filetype = "pdf"
    if len(sys.argv) == 2:
        filetype = sys.argv[1]

    # Generate the (x, y) data
    start = 0
    end = 1
    interval = 0.005
    xs = [x for x in np.arange(start, end + interval, interval)]
    results = [g(x) for x in xs]

    # Plot the data
    plt.plot(xs, results)

    # Save the graph
    plt.savefig("graph." + filetype)

    # Plot standard deviation lines
    for x in range(-3,4):
        plt.axvline(mu + (x * row), color="red")

    # Save the graph with standard deviation lines
    plt.savefig("graph-lines." + filetype)

if __name__ == '__main__':
    main()
