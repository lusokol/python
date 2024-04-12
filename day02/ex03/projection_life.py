from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
Use "life_expectancy_years.csv and \
income_per_person_gdppercapita_ppp_inflation_adjusted.csv \
as data to generate a graph with it.
    """
    income_data = load("life_expectancy_years.csv")
    life_expectancy_data = \
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    year = '1900'

    gdp_1900 = life_expectancy_data[year]
    life_expectancy_1900 = income_data[year]

    plt.scatter(gdp_1900, life_expectancy_1900)
    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
