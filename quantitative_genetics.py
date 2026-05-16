import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress, t

def calculate_heritability_with_levels(csv_filename):
    # Loads the data
    try:
        df = pd.read_csv(csv_filename, header=None)
    except FileNotFoundError:
        print(f"Error: Could not find '{csv_filename}'.")
        return

    # Ensure all data is numeric
    df = df.apply(pd.to_numeric, errors='coerce')

    #  Cleans Data & Remove Outliers
    df_clean = df[(df[0] >= 100) & (df[1] >= 100)].copy()

    # Calculate Variables
    df_clean['Mid-Parent'] = (df_clean[0] + df_clean[1]) / 2
    df_clean['Offspring_Mean'] = df_clean.iloc[:, 2:].mean(axis=1)

    # Drop any remaining rows missing crucial data
    df_clean = df_clean.dropna(subset=['Mid-Parent', 'Offspring_Mean'])
    
    X = df_clean['Mid-Parent'].values
    Y = df_clean['Offspring_Mean'].values
    n = len(X)

    # Perform Linear Regression
    slope, intercept, r_value, p_value, std_err = linregress(X, Y)
    h2 = slope

    # Calculate Confidence & Prediction Intervals
    x_line = np.linspace(X.min(), X.max(), 100)
    y_line = slope * x_line + intercept

    # Statistics for the intervals
    y_hat = slope * X + intercept
    residuals = Y - y_hat
    sse = np.sum(residuals**2)
    df_resid = n - 2
    mse = sse / df_resid 
    
    x_mean = np.mean(X)
    ssx = np.sum((X - x_mean)**2)
    
    t_stat = t.ppf(0.975, df_resid) 

    # Margins of error
    se_line = np.sqrt(mse * (1/n + (x_line - x_mean)**2 / ssx))
    ci_upper = y_line + t_stat * se_line
    ci_lower = y_line - t_stat * se_line

    se_pred = np.sqrt(mse * (1 + 1/n + (x_line - x_mean)**2 / ssx))
    pi_upper = y_line + t_stat * se_pred
    pi_lower = y_line - t_stat * se_pred

    # 6. Plot the Data and Levels
    plt.figure(figsize=(10, 7))
    
    plt.fill_between(x_line, pi_lower, pi_upper, color='#EAEAEA', alpha=0.8, 
                     label='95% Prediction Interval')
    plt.fill_between(x_line, ci_lower, ci_upper, color='#FFC0CB', alpha=0.7, 
                     label='95% Confidence Interval')

    plt.scatter(X, Y, color='#4A90E2', alpha=0.8, edgecolors='white', 
                s=50, label='Family Data Points', zorder=3)
    
    plt.plot(x_line, y_line, color='#E94A4A', linewidth=2.5, 
             label=f'Regression Line ($h^2$ = {h2:.2f})', zorder=4)

    plt.title('Mid-Parent Regression with 95% Confidence & Prediction Levels', 
              fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Mid-Parent Mean Height (cm)', fontsize=12)
    plt.ylabel('Offspring Mean Height (cm)', fontsize=12)
    plt.legend(loc='upper left', fontsize=10, framealpha=0.9)
    plt.grid(True, linestyle=':', alpha=0.6)
    
    print(f"Heritability (h^2) estimated at: {h2:.4f}")
    
    plt.tight_layout()
    plt.show()

# calculate_heritability_with_levels("Data for Quantitative Genetics.xlsx - Sheet1.csv")