import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax1 = plt.subplots()
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    intercept = result.intercept
    slope = result.slope
    years = pd.Series(range(1880, 2051))

    # Create first line of best fit
    ax1.plot(years, slope*years + intercept, 'r')

    df_2000 = df[df['Year'] >= 2000]
    result = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    intercept = result.intercept
    slope = result.slope
    years = pd.Series(range(2000, 2051))

    # Create second line of best fit
    ax1.plot(years, slope*years + intercept, 'g')

    ax1.set_title('Rise in Sea Level')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Sea Level (inches)')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()