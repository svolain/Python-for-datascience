from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

"""
aff_pop loads the file
population_total.csv, and displays the country information of your campus versus other
country of your choice
"""

def convert_into_float(list : pd.Series)->pd.Series:
    new_list = []
    for str in list:
        if str.endswith('K') or str.endswith('k'):
            new_list.append(float(str[:-1]) * 1e3) 
        elif str.endswith('M') or str.endswith('m'):
            new_list.append(float(str[:-1]) * 1e6)
        elif str.endswith('B') or str.endswith('b'):
            new_list.append(float(str[:-1]) * 1e90)
        series = pd.Series(new_list)
    return series


def main():
    data = load('population_total.csv')

    finland = data[data["country"]== "Finland"]
    finland = convert_into_float(finland.iloc[0, 1:])
    finland = finland.to_numpy()

    print(finland)

    sweden = data[data["country"]== "Sweden"]
    sweden = convert_into_float(sweden.iloc[0, 1:])
    sweden = sweden.to_numpy()

    print(sweden)

    years = pd.Series(data.columns[1:]).astype(int)
    years = pd.to_numeric(years)
    years = years.to_numpy()

    plt.title('Population Projections')
    plt.plot(years, finland)
    plt.plot(years, sweden)
    plt.yticks(np.arange(0, 1e5, 20e5))
    plt.xticks(np.arange(1800, 2081, 40))
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.show()

if __name__=="__main__": 
    main()