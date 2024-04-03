from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def main():
    df = load("life_expectancy_years.csv")
    index_ligne = df.index[df.iloc[:, 0] == 'France'].tolist()[0]
    ligne_specifique = df.iloc[index_ligne]
    print(ligne_specifique)

    # x = #1790, 2110
    # y = ligne_specifique[x]

    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')

    ax.set_xlabel('entry a')
    ax.set_ylabel('entry b')

    # fig, ax = plt.subplots()
    # ax.plot(x, y)
    plt.show()

if __name__ == '__main__':
    main()