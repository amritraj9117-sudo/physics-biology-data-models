# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd

# # The complete transcribed dataset (402 points)
# data = np.array([
#     8.43, 8.70, 5.02, -4.48, -7.04, 1.16, 8.42, 8.26, 5.02, -6.42,
#     -4.48, 8.41, -3.45, -7.12, 0.55, 8.24, 2.87, -5.91, -0.08, 7.54,
#     8.12, 4.48, -2.63, -8.63, 1.14, -5.57, -0.52, 0.67, -3.42, -8.47,
#     -8.91, 8.61, 2.92, 8.21, 0.48, 8.41, -8.22, -0.31, -4.14, 8.42,
#     -8.54, -8.77, -8.62, 5.87, 2.42, -8.66, -7.15, 8.50, -1.52, -2.36,
#     -8.20, -5.40, -8.50, 6.40, 2.40, -5.80, 6.10, 2.99, -1.09, -5.12,
#     -5.73, -2.64, 8.60, -7.54, 0.04, -0.81, 4.17, -3.24, 5.01, 4.90,
#     -7.80, 8.55, 6.55, 6.57, -7.99, -8.24, -1.11, -5.87, -8.61, -7.99,
#     -8.54, 8.40, -7.60, 8.50, 6.02, 0.08, -0.71, 8.35, 0.89, -8.22,
#     8.15, -2.53, 7.15, 2.74, 1.70, 1.69, -7.92, 4.53, 8.37, -4.34,
#     8.54, -3.75, 4.82, 3.15, -7.75, 8.57, -1.60, 8.01, 8.74, 8.14,
#     2.97, -8.01, 7.90, 1.40, 5.85, 8.57, 2.25, 5.87, -6.13, -7.02,
#     -6.91, -1.86, 8.57, 1.91, 8.34, 8.62, 8.57, 5.45, 5.19, 8.74,
#     -5.99, 8.72, 5.60, 2.12, 8.15, -1.53, 2.17, -8.22, -8.05, 8.55,
#     0.25, 5.11, -4.70, -4.55, 2.46, -6.82, 7.20, -6.42, -2.07, -5.37,
#     -8.07, 1.32, 7.51, 8.32, 2.25, 4.90, 5.30, 5.79, -7.16, 4.34,
#     -7.50, 4.52, 2.36, -4.70, -2.51, 4.40, 0.29, 8.01, 7.90, 4.02,
#     -1.98, -6.19, 3.14, 4.12, -5.84, 8.50, -2.47, 8.14, 1.61, 8.40,
#     0.42, -1.44, 6.18, -7.02, -0.60, 3.52, 8.76, 5.27, 2.26, -1.85,
#     5.10, 7.46, 8.52, 4.93, 0.70, -4.11, 8.26, -0.24, 8.72, 8.16,
#     7.49, 8.75, -7.80, -8.41, -1.04, 8.00, -8.60, -1.98, -8.42, 7.15,
#     -7.80, 3.50, 4.70, 8.76, -2.03, 8.01, -1.17, -8.06, 7.55, 8.74,
#     -3.28, 8.64, 5.75, -5.43, 7.62, 7.55, 3.98, 8.30, 4.54, -4.19,
#     6.78, 5.00, 8.32, 1.42, 8.73, 5.52, -0.37, 7.72, 7.31, 0.62,
#     8.25, 8.57, 7.63, 3.91, -2.54, 1.16, 0.40, 2.13, -8.29, 1.06,
#     2.48, 85.00, 0.16, 2.00, -3.35, 4.96, 4.31, -0.11, 6.54, 7.63,
#     -8.20, -0.16, 2.35, -8.52, 8.41, 0.12, 0.82, 2.01, -4.54, 8.22,
#     4.01, 8.62, 2.47, 5.02, -2.79, 8.79, 3.15, -8.31, 7.72, 6.52,
#     7.47, 8.54, -5.23, 8.54, 6.40, 0.19, 3.79, 7.14, -3.32, 4.52,
#     -4.14, 5.67, 7.20, 0.58, 6.78, 5.76, 6.13, 8.76, -8.41, -8.31,
#     4.40, -6.18, -8.72, -8.14, 3.79, -8.65, 6.12, 5.46, 1.07, 0.98,
#     2.92, 5.15, 8.78, -0.04, 0.48, 4.67, -5.83, -3.24, -7.91, 2.81,
#     -3.02, 5.37, 2.64, 6.14, 5.67, 8.50, -4.62, 0.44, -4.05, -7.24,
#     -8.54, -0.30, 8.72, 8.10, 8.75, 1.46, 3.42, 7.37, -0.60, 8.30,
#     3.24, 6.76, -8.64, -2.66, 5.34, -6.34, 0.12, 5.45, 2.93, 5.13,
#     -3.14, 8.48, 4.32, 0.05, -5.55, 3.54, -7.23, -8.02, 7.76, 8.54,
#     1.81, 1.62, -1.24, -4.36, -7.21, -7.78, 8.65, -1.76, -4.87, -0.97,
#     2.50, 7.27, 6.41, 5.62, 5.03, 8.32, 8.12, 4.51, 7.02, -6.01,
#     6.12, -2.92, -6.71, -8.42, 8.09, -0.30, -6.72, -7.21, 7.20, 8.07,
#     -7.60, 1.65, -5.81, -1.11, -2.15, -5.09, 8.54, -0.91, -8.25, -0.61,
#     6.52, -7.65, 4.92, 8.70, 1.89, 7.40, -7.04, -3.60, -7.52, 1.64,
#     4.20, 5.67, -8.58, 7.65, 7.81, -8.23, -7.65, -8.82, -8.56, 8.11,
#     7.94, 3.06, 1.52, 3.12, -5.04, -7.92, -8.88, 8.68, 8.67, -0.20,
#     -7.43, -1.13, 6.53, 3.20, 2.00, -6.23, -6.14, 8.10, 8.02, -8.65,
#     4.37, 0.23, -7.30, 0.01, 6.72, 8.53, 6.51, 7.31, -6.02, 2.09,
#     0.00, 8.71, 5.61, 1.72, -8.61, 4.41, 4.42, 2.13, 6.21, 2.44,
#     -5.65, -8.69, 1.46, 8.33, 8.76, 1.62, 2.37, -2.43, 8.64, -6.16,
#     -4.30, -4.26, -8.75, -6.93, -5.05, -2.86, -1.22
# ])

# # Remove the obvious outlier (85.00) which is likely a transcription error for 8.50
# data = np.where(data == 85.00, 8.50, data)

# V_0 = 9.0  # Peak voltage for binning

# # --- 1. Reconstructing Table 3.1 (Positive Half Analysis) ---
# pos_data = data[data >= 0]
# N_pos = len(pos_data)
# N_eff = 2 * N_pos  # Effective total N for formula

# bins = np.arange(0, V_0 + 0.5, 0.5)
# n_V, bin_edges = np.histogram(pos_data, bins=bins)

# # Calculate N_V (Cumulative Sum)
# N_V = np.cumsum(n_V)

# # Calculate Reconstructed V
# V_rec = V_0 * np.sin((np.pi * N_V) / N_eff)

# # Create DataFrame for Table
# table_df = pd.DataFrame({
#     'Bin Range': [f"{bin_edges[i]:.1f} - {bin_edges[i+1]:.1f}" for i in range(len(n_V))],
#     'n(V)': n_V,
#     'N_V': N_V,
#     'Recovered V': V_rec.round(2)
# })
# print("--- Data Table (Equivalent to Table 3.1) ---")
# print(table_df.to_string(index=False))

# # --- 2. Plotting Theoretical vs Experimental Distribution ---
# plt.figure(figsize=(12, 5))

# plt.subplot(1, 2, 1)
# # Experimental Histogram (All Data)
# all_bins = np.arange(-V_0, V_0 + 0.5, 0.5)
# plt.hist(data, bins=all_bins, density=True, alpha=0.5, color='lightgreen', edgecolor='green', label='Normalized n(V)')

# # Theoretical Curve
# v_theory = np.linspace(-V_0 + 0.1, V_0 - 0.1, 500)
# p_theory = 1 / (np.pi * np.sqrt(V_0**2 - v_theory**2))
# plt.plot(v_theory, p_theory, color='red', label=r'$P(V) = \frac{1}{\pi \sqrt{V_0^2 - V^2}}$')

# plt.xlabel('V')
# plt.ylabel('P(V) / Normalized n(V)')
# plt.title('Comparison of Theoretical and Experimental Data')
# plt.legend()

# # --- 3. Plotting Reconstructed Waveform ---
# plt.subplot(1, 2, 2)
# # Using bin centers for plotting
# bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
# plt.scatter(N_V, V_rec, facecolors='none', edgecolors='red', s=20, label='Recovered waveform')
# plt.xlabel('$N_V$')
# plt.ylabel(r'$V = V_0 \sin(\pi N_V / N)$')
# plt.title('One Fourth of Recovered Waveform')
# plt.legend()

# plt.tight_layout()
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit

# # 1. B vs Current Data
# # Solenoid Lengths in mm: 75, 100, 125
# curr_75 = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 4.8])
# b_75_curr = np.array([0, 16.8, 31.6, 47.6, 64.1, 79.8, 93.6, 108.5, 123.4, 140.2, 148.0])

# curr_100 = np.array([0, 0.5, 1, 1.5, 2.1, 2.5, 3, 3.5, 4, 4.5, 5])
# b_100_curr = np.array([0, 17.7, 35.1, 53.2, 73.6, 84.4, 100.5, 117.0, 133.3, 151.7, 164.8])

# curr_125 = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
# b_125_curr = np.array([0, 17.3, 35.4, 54.3, 69.3, 88.3, 104.6, 119.5, 137.0, 154.3, 171.6])

# # 2. B vs Position Data (Bench coordinates in cm)
# pos_75 = np.array([70.5, 69.5, 68.5, 67.5, 66.5, 65.5, 64.5, 63.5, 62.5, 61.5])
# b_75_pos = np.array([10.6, 29.5, 30.6, 33.4, 33.9, 33.7, 31.9, 26.7, 17.5, 9.1])

# pos_100 = np.array([72.5, 71.5, 70.5, 69.5, 68.5, 67.5, 66.5, 65.5, 64.5, 63.5, 62.5, 61.5])
# b_100_pos = np.array([11.2, 21.8, 29.4, 32.8, 34.6, 35.2, 35.1, 34.8, 33.6, 30.8, 24.2, 14.2])

# pos_125 = np.array([72.5, 71.5, 70.5, 69.5, 68.5, 67.5, 66.5, 65.5, 64.5, 63.5, 62.5, 61.5, 60.5])
# b_125_pos = np.array([10.9, 20.3, 28.9, 32.9, 34.4, 35.3, 35.7, 36.0, 36.0, 35.9, 35.5, 34.7, 33.1])

# # Linear function for B vs I
# def linear_func(x, m, c):
#     return m * x + c

# # Finite Solenoid function for B vs Position
# # B(x) = k * [ (x-x0 + L/2) / sqrt((x-x0 + L/2)^2 + R^2) - (x-x0 - L/2) / sqrt((x-x0 - L/2)^2 + R^2) ]
# def solenoid_func(x, k, x0, L, R):
#     # L and R in cm
#     term1 = (x - x0 + L/2) / np.sqrt((x - x0 + L/2)**2 + R**2)
#     term2 = (x - x0 - L/2) / np.sqrt((x - x0 - L/2)**2 + R**2)
#     return k * (term1 - term2)

# # Plotting B vs Current with Linear Fits
# plt.figure(figsize=(10, 6))
# for curr, b_val, label, length in zip([curr_75, curr_100, curr_125], 
#                                      [b_75_curr, b_100_curr, b_125_curr], 
#                                      ['L=75mm', 'L=100mm', 'L=125mm'],
#                                      [7.5, 10.0, 12.5]):
#     # Fit linear model
#     popt, _ = curve_fit(linear_func, curr, b_val)
#     plt.scatter(curr, b_val, label=f'Data {label}')
#     x_fit = np.linspace(min(curr), max(curr), 100)
#     plt.plot(x_fit, linear_func(x_fit, *popt), '--', label=f'Fit {label} (Slope={popt[0]:.2f})')

# plt.xlabel('Current (A)')
# plt.ylabel('Magnetic Field (Gauss)')
# plt.title('B vs I: Linear Best Fit')
# plt.legend()
# plt.grid(True)
# plt.show

# # Plotting B vs Position with Solenoid Profile Fits
# plt.figure(figsize=(10, 6))
# R_fixed = 1.6 # Fixed Radius 16mm = 1.6cm

# data_sets = [
#     (pos_75, b_75_pos, 7.5, 'L=75mm', 'blue'),
#     (pos_100, b_100_pos, 10.0, 'L=100mm', 'green'),
#     (pos_125, b_125_pos, 12.5, 'L=125mm', 'red')
# ]

# for x_data, y_data, L_fixed, label, color in data_sets:
#     # Function with L and R fixed
#     def fit_model(x, k, x0):
#         return solenoid_func(x, k, x0, L_fixed, R_fixed)
    
#     # Initial guess: max field/2 (k), mean position (x0)
#     popt, _ = curve_fit(fit_model, x_data, y_data, p0=[max(y_data)/2, np.mean(x_data)])
    
#     plt.scatter(x_data, y_data, color=color, label=f'Data {label}')
#     x_fine = np.linspace(min(x_data)-1, max(x_data)+1, 200)
#     plt.plot(x_fine, fit_model(x_fine, *popt), color=color, linestyle='--', label=f'Fit {label}')

# plt.xlabel('Position on Bench (cm)')
# plt.ylabel('Magnetic Field (Gauss)')
# plt.title('B vs Position: Finite Solenoid Theoretical Fit')
# plt.legend()
# plt.grid(True)
# plt.show
# import numpy as np
# import matplotlib.pyplot as plt

# def simulate_drift(N_individuals, generations, runs, initial_p=0.5):
#     """
#     Simulates genetic drift using the Wright-Fisher model.
#     N_individuals: Number of diploid individuals (2N alleles)
#     """
#     final_frequencies = []
#     alleles = 2 * N_individuals
    
#     for _ in range(runs):
#         p = initial_p
#         for _ in range(generations):
#             # Draw the next generation's allele count from a binomial distribution
#             A1_count = np.random.binomial(alleles, p)
#             p = A1_count / alleles
        
#         # Round to the nearest 0.05 as requested by the assignment
#         rounded_p = round(p * 20) / 20
#         final_frequencies.append(rounded_p)
        
#     return final_frequencies

# # Run parameters
# generations = 20
# runs = 50

# # Part a: Census size N=16
# freqs_16 = simulate_drift(16, generations, runs)

# # Part b: Effective size N=9
# freqs_9 = simulate_drift(9, generations, runs)


# # --- Plotting the Histograms Separately ---
# bins = np.arange(-0.025, 1.075, 0.05) # Centered bins for 0.0, 0.05, 0.10, etc.

# # First Graph: N=16
# plt.figure(figsize=(8, 5))
# plt.hist(freqs_16, bins=bins, edgecolor='black', color='skyblue')
# plt.title("Part A: Final Frequencies after 20 Generations (N = 16)")
# plt.xlabel("Final frequency of allele A1")
# plt.ylabel("Number of runs")
# plt.xlim(-0.05, 1.05)
# plt.xticks(np.arange(0, 1.1, 0.1))
# plt.grid(True)
# plt.tight_layout()
# plt.show() # Displays the first graph

# # Second Graph: N=9
# plt.figure(figsize=(8, 5))
# plt.hist(freqs_9, bins=bins, edgecolor='black', color='salmon')
# plt.title("Part B: Final Frequencies after 20 Generations (N = 9)")
# plt.xlabel("Final frequency of allele A1")
# plt.ylabel("Number of runs")
# plt.xlim(-0.05, 1.05)
# plt.xticks(np.arange(0, 1.1, 0.1))
# plt.tight_layout()
# plt.show() # Displays the second graph
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.integrate import odeint

# # DESCRIPTION:
# # This script models a Genetic Toggle Switch (Mutual Inhibition between Gene U and Gene V).
# # It demonstrates how a system can exhibit "Bistability" (two stable states).
# # This is a foundational concept in Systems Biology and Cell Fate Decision making.

# def toggle_switch(y, t, alpha1, alpha2, beta, gamma):
#     """
#     Defines the differential equations for two mutually inhibiting genes.
#     u: Concentration of Protein U
#     v: Concentration of Protein V
#     alpha: Production rate
#     beta: Cooperativity (Hill coefficient)
#     gamma: Degradation rate
#     """
#     u, v = y
    
#     # Hill function for repression
#     du_dt = (alpha1 / (1 + v**beta)) - gamma * u
#     dv_dt = (alpha2 / (1 + u**beta)) - gamma * v
    
#     return [du_dt, dv_dt]

# # --- PARAMETERS ---
# alpha1 = 10.0  # Production rate of U
# alpha2 = 10.0  # Production rate of V
# beta = 2.5     # Hill coefficient (Cooperativity) -> High beta = steep switch
# gamma = 1.0    # Degradation rate

# # Time points for simulation
# t = np.linspace(0, 50, 1000)

# # --- SIMULATION 1: Start with high U, low V ---
# y0_A = [10.0, 0.1] 
# solution_A = odeint(toggle_switch, y0_A, t, args=(alpha1, alpha2, beta, gamma))

# # --- SIMULATION 2: Start with low U, high V ---
# y0_B = [0.1, 10.0]
# solution_B = odeint(toggle_switch, y0_B, t, args=(alpha1, alpha2, beta, gamma))

# # --- PLOTTING ---
# plt.figure(figsize=(10, 5))

# # Plot 1: Case A (U wins)
# plt.subplot(1, 2, 1)
# plt.plot(t, solution_A[:, 0], 'r-', label='Protein U (High)')
# plt.plot(t, solution_A[:, 1], 'b--', label='Protein V (Low)')
# plt.title('Initial Condition: High U')
# plt.xlabel('Time')
# plt.ylabel('Concentration')
# plt.legend()
# plt.grid(True)

# # Plot 2: Case B (V wins)
# plt.subplot(1, 2, 2)
# plt.plot(t, solution_B[:, 0], 'r-', label='Protein U (Low)')
# plt.plot(t, solution_B[:, 1], 'b--', label='Protein V (High)')
# plt.title('Initial Condition: High V')
# plt.xlabel('Time')
# plt.ylabel('Concentration')
# plt.legend()
# plt.grid(True)

# plt.suptitle('Genetic Toggle Switch: Bistability Demonstration')
# plt.tight_layout()
# plt.show()
# import pandas as pd
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import linregress, t

# def calculate_heritability_with_levels(csv_filename):
#     # 1. Load the data
#     try:
#         # Assuming no header in your raw data
#         df = pd.read_csv(csv_filename, header=None)
#     except FileNotFoundError:
#         print(f"Error: Could not find '{csv_filename}'.")
#         return

#     # Ensure all data is numeric
#     df = df.apply(pd.to_numeric, errors='coerce')

#     # 2. Clean Data & Remove Outliers (Heights must be >= 100 cm)
#     df_clean = df[(df[0] >= 100) & (df[1] >= 100)].copy()

#     # 3. Calculate Variables
#     df_clean['Mid-Parent'] = (df_clean[0] + df_clean[1]) / 2
#     # Offspring start at column 2. Average them, ignoring NaNs.
#     df_clean['Offspring_Mean'] = df_clean.iloc[:, 2:].mean(axis=1)

#     # Drop any remaining rows missing crucial data
#     df_clean = df_clean.dropna(subset=['Mid-Parent', 'Offspring_Mean'])
    
#     X = df_clean['Mid-Parent'].values
#     Y = df_clean['Offspring_Mean'].values
#     n = len(X)

#     # 4. Perform Linear Regression
#     slope, intercept, r_value, p_value, std_err = linregress(X, Y)
#     h2 = slope

#     # 5. Calculate Confidence & Prediction Intervals ("Levels")
#     x_line = np.linspace(X.min(), X.max(), 100)
#     y_line = slope * x_line + intercept

#     # Statistics for the intervals
#     y_hat = slope * X + intercept # Predicted values
#     residuals = Y - y_hat
#     sse = np.sum(residuals**2) # Sum of squared errors
#     df_resid = n - 2 # Degrees of freedom
#     mse = sse / df_resid # Mean squared error
    
#     # Standard Error calculations
#     x_mean = np.mean(X)
#     ssx = np.sum((X - x_mean)**2) # Sum of squares for X
    
#     # t-statistic for 95% confidence level
#     t_stat = t.ppf(0.975, df_resid) 

#     # Margin of error for Confidence Interval (CI)
#     se_line = np.sqrt(mse * (1/n + (x_line - x_mean)**2 / ssx))
#     ci_upper = y_line + t_stat * se_line
#     ci_lower = y_line - t_stat * se_line

#     # Margin of error for Prediction Interval (PI)
#     se_pred = np.sqrt(mse * (1 + 1/n + (x_line - x_mean)**2 / ssx))
#     pi_upper = y_line + t_stat * se_pred
#     pi_lower = y_line - t_stat * se_pred

#     # 6. Plot the Data and Levels
#     plt.figure(figsize=(10, 7))
    
#     # Plot Prediction Interval (Outer Level)
#     plt.fill_between(x_line, pi_lower, pi_upper, color='#EAEAEA', alpha=0.8, 
#                      label='95% Prediction Interval')

#     # Plot Confidence Interval (Inner Level)
#     plt.fill_between(x_line, ci_lower, ci_upper, color='#FFC0CB', alpha=0.7, 
#                      label='95% Confidence Interval')

#     # Scatter plot of actual families
#     plt.scatter(X, Y, color='#4A90E2', alpha=0.8, edgecolors='white', 
#                 s=50, label='Family Data Points', zorder=3)
    
#     # Regression Line
#     plt.plot(x_line, y_line, color='#E94A4A', linewidth=2.5, 
#              label=f'Regression Line ($h^2$ = {h2:.2f})', zorder=4)

#     # Formatting
#     plt.title('Mid-Parent Regression with 95% Confidence & Prediction Levels', 
#               fontsize=14, fontweight='bold', pad=15)
#     plt.xlabel('Mid-Parent Mean Height (cm)', fontsize=12)
#     plt.ylabel('Offspring Mean Height (cm)', fontsize=12)
#     plt.legend(loc='upper left', fontsize=10, framealpha=0.9)
#     plt.grid(True, linestyle=':', alpha=0.6)
    
#     # Print results
#     print(f"Heritability (h^2) estimated at: {h2:.4f}")
    
#     plt.tight_layout()
#     plt.show()

# # Run the function (ensure your CSV is saved as class_heights.csv)
# calculate_heritability_with_levels("C:/Users/Amrit Raj/Downloads/Data for Quantitative Genetics.xlsx - Sheet1.csv")
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import linregress

# def calculate_heritability(csv_filename):
#     # 1. Load the data
#     try:
#         df = pd.read_csv(csv_filename)
#         print(f"Successfully loaded {len(df)} families from {csv_filename}\n")
#     except FileNotFoundError:
#         print(f"Error: Could not find '{csv_filename}'.")
#         print("Please ensure your spreadsheet is saved as a CSV in the same folder.")
#         return

#     # 2. Calculate the Mid-Parent Height (X axis)
#     # iloc[:, 0] gets the 1st column (Mother), iloc[:, 1] gets the 2nd (Father)
#     df['Mid-Parent'] = (df.iloc[:, 0] + df.iloc[:, 1]) / 2

#     # 3. Calculate the Offspring Mean Height (Y axis)
#     # iloc[:, 2:] grabs the 3rd column onward (Your height + all siblings)
#     # .mean(axis=1) averages them together, automatically ignoring any blank (NaN) cells
#     df['Offspring_Mean'] = df.iloc[:, 2:].mean(axis=1)

#     # 4. Clean the data (drop rows if someone forgot to enter parent/offspring data)
#     df_clean = df.dropna(subset=['Mid-Parent', 'Offspring_Mean'])
    
#     X = df_clean['Mid-Parent']
#     Y = df_clean['Offspring_Mean']

#     # 5. Perform Mid-Parent Regression
#     # The slope of this regression line is the narrow-sense heritability (h^2)
#     slope, intercept, r_value, p_value, std_err = linregress(X, Y)
    
#     h2 = slope

#     # 6. Print the statistical results
#     print("-" * 30)
#     print("REGRESSION RESULTS")
#     print("-" * 30)
#     print(f"Heritability (h^2) : {h2:.4f}")
#     print(f"R-squared          : {r_value**2:.4f}")
    

#     # 7. Plot the data
#     plt.figure(figsize=(9, 6))
    
#     # Scatter plot of the actual family data
#     plt.scatter(X, Y, color='#4A90E2', alpha=0.7, edgecolors='k', label='Family Data Points')

#     # Calculate points for the trendline
#     x_line = np.linspace(X.min(), X.max(), 100)
#     y_line = slope * x_line + intercept
    
#     # Draw the regression line
#     plt.plot(x_line, y_line, color='#E94A4A', linewidth=2, 
#              label=f'Regression Line ($h^2$ = {h2:.2f})')

#     # Formatting the chart
#     plt.title('Mid-Parent Regression for Height', fontsize=14, fontweight='bold')
#     plt.xlabel('Mid-Parent Mean Height (cm)', fontsize=12)
#     plt.ylabel('Offspring Mean Height (cm)', fontsize=12)
#     plt.legend(fontsize=11)
#     plt.grid(True, linestyle='--', alpha=0.5)
    
#     # Show the plot
#     plt.tight_layout()
#     plt.show()

# # Run the function using your file name
# calculate_heritability("C:/Users/Amrit Raj/Downloads/class height.csv")
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import linregress, zscore
# import tensorflow as tf

# def detect_height_anomalies(csv_filename):
#     # 1. Load and prepare data
#     try:
#         df = pd.read_csv(csv_filename, header=None)
#     except FileNotFoundError:
#         print(f"Error: Could not find '{csv_filename}'")
#         return

#     df = df.apply(pd.to_numeric, errors='coerce')
#     df['Mid-Parent'] = (df[0] + df[1]) / 2
#     df['Offspring_Mean'] = df.iloc[:, 2:].mean(axis=1)
#     df['Original_Row'] = df.index + 1 # Keep track of row numbers
#     df = df.dropna(subset=['Mid-Parent', 'Offspring_Mean'])

#     # 2. Find Extreme Anomalies (Data entry errors)
#     # Flagging anything under 100cm or over 230cm
#     extreme_mask = (df['Mid-Parent'] < 100) | (df['Mid-Parent'] > 230) | \
#                    (df['Offspring_Mean'] < 100) | (df['Offspring_Mean'] > 230)
    
#     extreme_anomalies = df[extreme_mask].copy()
    
#     # Remove extreme anomalies before fitting the trendline
#     df_valid = df.drop(extreme_anomalies.index).copy()

#     # 3. Find Trend Anomalies (Residual Analysis)
#     # Fit the regression line
#     slope, intercept, _, _, _ = linregress(df_valid['Mid-Parent'], df_valid['Offspring_Mean'])
    
#     # Calculate Expected Height & Residuals (Actual - Expected)
#     df_valid['Expected_Offspring'] = slope * df_valid['Mid-Parent'] + intercept
#     df_valid['Residual'] = df_valid['Offspring_Mean'] - df_valid['Expected_Offspring']
    
#     # Calculate Z-score of the residuals (Standard deviations away from the line)
#     df_valid['Residual_Z_Score'] = zscore(df_valid['Residual'])
    
#     # Flag points with an absolute Z-score > 2.5
#     trend_anomalies = df_valid[np.abs(df_valid['Residual_Z_Score']) > 2.5].copy()

#     # 4. Print Results
#     print("\n--- EXTREME VALUE ANOMALIES (Data Entry Errors) ---")
#     print(extreme_anomalies[['Original_Row', 'Mid-Parent', 'Offspring_Mean']])

#     print("\n--- TREND ANOMALIES (High deviation from regression) ---")
#     print(trend_anomalies[['Original_Row', 'Mid-Parent', 'Offspring_Mean', 'Residual']])

#     # 5. Plotting
#     plt.figure(figsize=(10, 7))

#     # Normal Data Points
#     normal_points = df_valid.drop(trend_anomalies.index)
#     plt.scatter(normal_points['Mid-Parent'], normal_points['Offspring_Mean'], 
#                 color="#5B636D", alpha=0.6, label='Normal Data', zorder=2)

#     # Highlight Trend Anomalies in Orange
#     plt.scatter(trend_anomalies['Mid-Parent'], trend_anomalies['Offspring_Mean'], 
#                 color='#FFA500', edgecolor='black', s=90, label='Trend Anomalies', zorder=3)

#     # Highlight Extreme Anomalies in Red (X markers)
#     plt.scatter(extreme_anomalies['Mid-Parent'], extreme_anomalies['Offspring_Mean'], 
#                 color="#3B3131", edgecolor='black', marker='X', s=100, label='Extreme Errors', zorder=3)

#     # Draw Regression Line
#     x_vals = np.array([df_valid['Mid-Parent'].min(), df_valid['Mid-Parent'].max()])
#     plt.plot(x_vals, intercept + slope * x_vals, color='black', linestyle='--', label='Regression Line')

#     plt.title('Mid-Parent Regression: Anomaly Detection', fontsize=14, fontweight='bold')
#     plt.xlabel('Mid-Parent Mean Height (cm)')
#     plt.ylabel('Offspring Mean Height (cm)')
#     plt.legend()
#     plt.grid(True, linestyle=':', alpha=0.6)
#     plt.tight_layout()
#     plt.show()

# # Run the function
# # detect_height_anomalies("C:/Users/Amrit Raj/Downloads/Data for Quantitative Genetics.xlsx - Sheet1.csv"
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model
# Load the data
oecd_bli = pd.read_csv("C:/Users/Amrit Raj/Downloads/housing_data.csv")
print(oecd_bli)