import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    fig, ax = plt.subplots()

    fs = 18

    with open("log/pursuit.log", "r") as f:
        for line in f:
            line = line.strip().split()
            loss = line[1].split()[1][1:-1].split(',')
            print loss
