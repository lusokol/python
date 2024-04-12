from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
Use "life_expectancy_years.csv as data to generate a graph with it.
    """
    dataset = load("life_expectancy_years.csv")
    fr_data = dataset[dataset["country"] == "France"]
    years = fr_data.columns[1:]
    country = fr_data.values[0, 1:]
    plt.plot(years, country)
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.xticks(years[::40], rotation=0)
    plt.ylabel("Life expectancy")
    plt.yticks(range(30, 91, 10))
    plt.show()


if __name__ == '__main__':
    main()
