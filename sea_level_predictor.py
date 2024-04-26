import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, axes = plt.subplots(figsize = (10,10))
    plt.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'],)
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level (inches)')
    axes.set_title('Rise in Sea Level')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = np.arange(1880, 2050, 1)
    reg_line = [slope * xi + intercept for xi in years]
    plt.plot(years, reg_line, color = 'red', label = 'Fit line 1')

    # Create second line of best fit
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_limit = np.arange(2000, 2050, 1)
    reg_line2 = [slope2 * xj + intercept for xj in years_limit]
    plt.plot(years_limit, reg_line2, color = 'blue', label = 'Fit line 2')
    plt.show()

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()