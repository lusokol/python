from load_csv import load
import matplotlib.pyplot as plt


def toNumber(pop_str):
    """
   Turn million and thousand into number.
   15.7k => 15700
   1.75M => 1750000
    """
    if pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)


def main():
    """
Use "population_total.csv as data to generate a graph with it.
    """
    country1 = "France"
    country2 = "Belgium"

    dataset = load("population_total.csv")

    try:
        c1_data = dataset[dataset['country'] == country1].iloc[:, 1:]
        c2_data = dataset[dataset['country'] == country2].iloc[:, 1:]

        years = c1_data.columns.astype(int)
        years = years[years <= 2050]

        c1_pop = c1_data.values.flatten()
        c2_pop = c2_data.values.flatten()

        c1_pop = [toNumber(pop) for pop in c1_pop]
        c2_pop = [toNumber(pop) for pop in c2_pop]

        c1_pop = c1_pop[:len(years)]
        c2_pop = c2_pop[:len(years)]

        # lines
        plt.plot(years, c2_pop, label=country2, color="blue")
        plt.plot(years, c1_pop, label=country1, color="green")

        plt.title("Population Projections")

        # X parameters
        plt.xlabel("Year")
        plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
        plt.xlim(1790, 2060)

        # Y parameters
        plt.ylabel("Population")
        pop_max = max(max(c1_pop), max(c2_pop))
        y_ticks = [i * 2e7 for i in range(int((pop_max / 1e7 / 2) + 1))][1:]
        plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])

        plt.legend(loc='lower right')
        plt.show()
        # print(list(range(1800, 2051, 40)))
    except IndexError as error:
        print(f"IndexError: {error}")
    except KeyError as error:
        print(f"KeyError: {error}")
    except ValueError as error:
        print(f"ValueError: {error}")
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Forcequit")


if __name__ == '__main__':
    main()
