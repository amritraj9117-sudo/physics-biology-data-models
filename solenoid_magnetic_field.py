import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. B vs Current Data
# Solenoid Lengths in mm: 75, 100, 125
curr_75 = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 4.8])
b_75_curr = np.array([0, 16.8, 31.6, 47.6, 64.1, 79.8, 93.6, 108.5, 123.4, 140.2, 148.0])

curr_100 = np.array([0, 0.5, 1, 1.5, 2.1, 2.5, 3, 3.5, 4, 4.5, 5])
b_100_curr = np.array([0, 17.7, 35.1, 53.2, 73.6, 84.4, 100.5, 117.0, 133.3, 151.7, 164.8])

curr_125 = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
b_125_curr = np.array([0, 17.3, 35.4, 54.3, 69.3, 88.3, 104.6, 119.5, 137.0, 154.3, 171.6])

# 2. B vs Position Data (Bench coordinates in cm)
pos_75 = np.array([70.5, 69.5, 68.5, 67.5, 66.5, 65.5, 64.5, 63.5, 62.5, 61.5])
b_75_pos = np.array([10.6, 29.5, 30.6, 33.4, 33.9, 33.7, 31.9, 26.7, 17.5, 9.1])

pos_100 = np.array([72.5, 71.5, 70.5, 69.5, 68.5, 67.5, 66.5, 65.5, 64.5, 63.5, 62.5, 61.5])
b_100_pos = np.array([11.2, 21.8, 29.4, 32.8, 34.6, 35.2, 35.1, 34.8, 33.6, 30.8, 24.2, 14.2])

pos_125 = np.array([72.5, 71.5, 70.5, 69.5, 68.5, 67.5, 66.5, 65.5, 64.5, 63.5, 62.5, 61.5, 60.5])
b_125_pos = np.array([10.9, 20.3, 28.9, 32.9, 34.4, 35.3, 35.7, 36.0, 36.0, 35.9, 35.5, 34.7, 33.1])

# Linear function for B vs I
def linear_func(x, m, c):
    return m * x + c

# Finite Solenoid function for B vs Position
# B(x) = k * [ (x-x0 + L/2) / sqrt((x-x0 + L/2)^2 + R^2) - (x-x0 - L/2) / sqrt((x-x0 - L/2)^2 + R^2) ]
def solenoid_func(x, k, x0, L, R):
    # L and R in cm
    term1 = (x - x0 + L/2) / np.sqrt((x - x0 + L/2)**2 + R**2)
    term2 = (x - x0 - L/2) / np.sqrt((x - x0 - L/2)**2 + R**2)
    return k * (term1 - term2)

# Plotting B vs Current with Linear Fits
plt.figure(figsize=(10, 6))
for curr, b_val, label, length in zip([curr_75, curr_100, curr_125], 
                                     [b_75_curr, b_100_curr, b_125_curr], 
                                     ['L=75mm', 'L=100mm', 'L=125mm'],
                                     [7.5, 10.0, 12.5]):
    # Fit linear model
    popt, _ = curve_fit(linear_func, curr, b_val)
    plt.scatter(curr, b_val, label=f'Data {label}')
    x_fit = np.linspace(min(curr), max(curr), 100)
    plt.plot(x_fit, linear_func(x_fit, *popt), '--', label=f'Fit {label} (Slope={popt[0]:.2f})')

plt.xlabel('Current (A)')
plt.ylabel('Magnetic Field (Gauss)')
plt.title('B vs I: Linear Best Fit')
plt.legend()
plt.grid(True)
plt.show()

# Plotting B vs Position with Solenoid Profile Fits
plt.figure(figsize=(10, 6))
R_fixed = 1.6 # Fixed Radius 16mm = 1.6cm

data_sets = [
    (pos_75, b_75_pos, 7.5, 'L=75mm', 'blue'),
    (pos_100, b_100_pos, 10.0, 'L=100mm', 'green'),
    (pos_125, b_125_pos, 12.5, 'L=125mm', 'red')
]

for x_data, y_data, L_fixed, label, color in data_sets:
    # Function with L and R fixed
    def fit_model(x, k, x0):
        return solenoid_func(x, k, x0, L_fixed, R_fixed)
    
    # Initial guess: max field/2 (k), mean position (x0)
    popt, _ = curve_fit(fit_model, x_data, y_data, p0=[max(y_data)/2, np.mean(x_data)])
    
    plt.scatter(x_data, y_data, color=color, label=f'Data {label}')
    x_fine = np.linspace(min(x_data)-1, max(x_data)+1, 200)
    plt.plot(x_fine, fit_model(x_fine, *popt), color=color, linestyle='--', label=f'Fit {label}')

plt.xlabel('Position on Bench (cm)')
plt.ylabel('Magnetic Field (Gauss)')
plt.title('B vs Position: Finite Solenoid Theoretical Fit')
plt.legend()
plt.grid(True)
plt.show()