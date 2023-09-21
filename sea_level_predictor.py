import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level']) 

    x = list(range(1880, 2051)) 
    y = [intercept + slope * year for year in x]
    plt.plot(x, y, color='red', label='Line of Best Fit')



    # Create second line of best fit
    df_filtered = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_filtered['Year'], df_filtered['CSIRO Adjusted Sea Level'])
    x = list(range(2000, 2051))
    y = [intercept + slope * year for year in x]
    plt.plot(x, y, color='green', label='New Line of Best Fit')
    





    plt.legend()
    
    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

