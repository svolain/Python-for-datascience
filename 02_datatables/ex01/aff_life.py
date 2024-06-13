from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def main():
    data = load('life_expectancy_years.csv')

    finland = data[data["country"]== "Finland"]
    finland = finland.iloc[0, 1:]
    finland = finland.to_numpy()


    years = pd.Series(data.columns[1:]).astype(int)
    years = pd.to_numeric(years)
    years = years.to_numpy()

    plt.title('Finland Life Expectancy Projections')
    plt.plot(years, finland)
    plt.yticks(np.arange(0, 91, 10))
    plt.xticks(np.arange(1800, 2081, 40))
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title('Finland Life Expectancy Projections')
    plt.show()
if __name__=="__main__": 
    main()
