import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression

# DATA

# Magnetic field vs Current Data (Sensor at the center and increasing the current)
curr_75 = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 4.8])
b_75_curr = np.array([0, 16.8, 31.6, 47.6, 64.1, 79.8, 93.6, 108.5, 123.4, 140.2, 148.0])

curr_100 = np.array([0, 0.5, 1, 1.5, 2.1, 2.5, 3, 3.5, 4, 4.5, 5])
b_100_curr = np.array([0, 17.7, 35.1, 53.2, 73.6, 84.4, 100.5, 117.0, 133.3, 151.7, 164.8])

curr_125 = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
b_125_curr = np.array([0, 17.3, 35.4, 54.3, 69.3, 88.3, 104.6, 119.5, 137.0, 154.3, 171.6])

# Magnetic Field vs Position Data (observing the change in the magnetic feild at different postion of sensor)
pos_75 = np.array([70.5, 69.5, 68.5, 67.5, 66.5, 65.5, 64.5, 63.5, 62.5, 61.5])
b_75_pos = np.array([10.6, 29.5, 30.6, 33.4, 33.9, 33.7, 31.9, 26.7, 17.5, 9.1])

pos_100 = np.array([72.5, 71.5, 70.5, 69.5, 68.5, 67.5, 66.5, 65.5, 64.5, 63.5, 62.5, 61.5])
b_100_pos = np.array([11.2, 21.8, 29.4, 32.8, 34.6, 35.2, 35.1, 34.8, 33.6, 30.8, 24.2, 14.2])

pos_125 = np.array([72.5, 71.5, 70.5, 69.5, 68.5, 67.5, 66.5, 65.5, 64.5, 63.5, 62.5, 61.5, 60.5])
b_125_pos = np.array([10.9, 20.3, 28.9, 32.9, 34.4, 35.3, 35.7, 36.0, 36.0, 35.9, 35.5, 34.7, 33.1]) 


# MODEL FUNCTIONS

def solenoid_func(x, k, x0, L, R):
    """Finite Solenoid profile equation for B vs Position (L and R in cm)."""
    term1 = (x - x0 + L/2) / np.sqrt((x - x0 + L/2)**2 + R**2)
    term2 = (x - x0 - L/2) / np.sqrt((x - x0 - L/2)**2 + R**2)
    return k * (term1 - term2)


#  LINEAR REGRESSION AND PLOTTING (B vs I) 

print("--- Linear Regression Results (B vs I) ---")
plt.figure(figsize=(10, 6))

datasets_curr = [
    (curr_75, b_75_curr, 'L=75mm'),
    (curr_100, b_100_curr, 'L=100mm'),
    (curr_125, b_125_curr, 'L=125mm')
]

for curr, b_val, label in datasets_curr:
    X = curr.reshape(-1, 1)
    
    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X, b_val)
    
    # Extract fit parameters
    slope = model.coef_[0]
    intercept = model.intercept_
    r2 = model.score(X, b_val)  
    
    print(f"{label}: Slope = {slope:.4f}, Intercept = {intercept:.4f}, R² = {r2:.4f}")
    
    # Plot experimental data points
    plt.scatter(curr, b_val, label=f'Data {label}')
    
    # Generate prediction line 
    x_fit = np.linspace(min(curr), max(curr), 100).reshape(-1, 1)
    y_fit = model.predict(x_fit)
    plt.plot(x_fine_linear := x_fit.flatten(), y_fit, '--', label=f'Fit {label} (R²={r2:.4f})')

plt.xlabel('Current (A)')
plt.ylabel('Magnetic Field (Gauss)')
plt.title('B vs I: Linear Best Fit (scikit-learn)')
plt.legend()
plt.grid(True)
plt.show()


# 4. FIELD PROFILE PLOTTING (B vs Position)

plt.figure(figsize=(10, 6))
R_fixed = 1.6  # Fixed Radius of the solenoid 16mm = 1.6cm

data_sets_pos = [
    (pos_75, b_75_pos, 7.5, 'L=75mm', 'blue', 'o'),
    (pos_100, b_100_pos, 10.0, 'L=100mm', 'green', 's'),
    (pos_125, b_125_pos, 12.5, 'L=125mm', 'red', '^')
]

for x_data, y_data, L_fixed, label, color, marker_shape in data_sets_pos:
    
    def fit_model(x, k, x0):
        return solenoid_func(x, k, x0, L_fixed, R_fixed)
    
    # Initial guess optimization setup
    popt, _ = curve_fit(fit_model, x_data, y_data, p0=[max(y_data)/2, np.mean(x_data)])
    
    # Plotting scatter points
    plt.scatter(x_data, y_data, color=color, marker=marker_shape, s=60, label=f'Data {label}')
    
    # Generate smooth fitted curve lines
    x_fine = np.linspace(min(x_data)-1, max(x_data)+1, 200)
    plt.plot(x_fine, fit_model(x_fine, *popt), color=color, linestyle='--', label=f'Fit {label}')

plt.xlabel('Position on Bench (cm)')
plt.ylabel('Magnetic Field (Gauss)')
plt.title('B vs Position: Finite Solenoid Theoretical Fit')
plt.legend()
plt.grid(True)
plt.show()
