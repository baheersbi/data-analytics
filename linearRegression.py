# Re-attempting to plot the data and regression line
import numpy as np
import matplotlib.pyplot as plt


# Calculate slope and intercept manually
def calculate_slope_intercept(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - (slope * x1)
    return slope, intercept


# Define two points
point1 = (2, 54)
point2 = (9, 81)
point3 = (12, 98)

# Calculate slope and intercept
m, b = calculate_slope_intercept(point1[0], point1[1], point2[0], point2[1])

# Prepare data for plotting
x_values = np.linspace(0, 10, 100)  # Get 100 evenly spaced values between 0 and 10
y_values = m * x_values + b  # Apply the linear regression formula

# Plotting the original points and the regression line
plt.scatter([point1[0], point2[0]], [point1[1], point2[1]], color='red', label='Data Points')
plt.plot(x_values, y_values, label='Regression Line', color='blue')
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.legend()
plt.grid(True)
plt.show()

# Return the calculated slope and intercept
(m, b)
