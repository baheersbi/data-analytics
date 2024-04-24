import numpy as np
import matplotlib.pyplot as plt


# Calculate slope and intercept using the least squares method
def calculate_slope_intercept(x_vals, y_vals):
    A = np.vstack([x_vals, np.ones(len(x_vals))]).T
    slope, intercept = np.linalg.lstsq(A, y_vals, rcond=None)[0]
    return slope, intercept


# Define an array of data points
points = np.array([(2, 54), (9, 81), (12, 98), (15, 111), (18, 130), (19, 190)])  # Example points

# Extract x and y values from the points
x_vals = points[:, 0]
y_vals = points[:, 1]

# Calculate slope and intercept
m, b = calculate_slope_intercept(x_vals, y_vals)

# Prepare data for plotting
x_values = np.linspace(min(x_vals), max(x_vals), 100)  # Range of x values
y_values = m * x_values + b  # Apply the linear regression formula

# Plotting the original points and the regression line
plt.scatter(x_vals, y_vals, color='red', label='Data Points')
plt.plot(x_values, y_values, label='Regression Line', color='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Regression Example')
plt.legend()
plt.grid(True)
plt.show()

# Return the calculated slope and intercept
print("Slope (m):", m)
print("Intercept (b):", b)
