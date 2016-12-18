import math
import matplotlib.pyplot as plt
import numpy as np
import sys

mu  = 0.5445663 # Mean
row = 0.1208535 # Standard deviation

def main():
    # Determine the graph file type
    filetype = "pdf"
    if len(sys.argv) == 3:
        filetype = sys.argv[2]

    if len(sys.argv) > 1:
        data_file = sys.argv[1]
        ys = [float(line) for line in open(data_file, 'r').read().split("\n")[0:-1]]
        xs = range(0, len(ys))
        plot(xs, ys, filetype)

def plot(xs, ys, filetype):
    # Plot the data
    plt.scatter(xs, ys)
    plt.title("RR Lyrae Periods")
    plt.xlabel("Id number")
    plt.ylabel("Period (days)")

    # Save the graph
    plt.savefig("scatter-graph." + filetype)

    # Plot standard deviation lines
    for x in range(-3,4):
        if x == 0:
            plt.axhline(mu + (x * row), color="red")
        else:
            plt.axhline(mu + (x * row), color="green")

    # Save the graph with standard deviation lines
    plt.savefig("scatter-graph-lines." + filetype)

if __name__ == '__main__':
    main()
