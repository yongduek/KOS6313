import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Draw 1000 samples from a standard normal distribution
theta_samples_standard_normal = np.random.normal(0, 1, 100000)

# Define the logistic function
def logistic(x):
    return 1 / (1 + np.exp(-x))

# Generate a range of theta values for plotting
theta_range = np.linspace(-5, 5, 1000)

# Compute eta values using the logistic function
eta_values = logistic(theta_range)

# Transform theta to eta for density plot
eta_samples_standard_normal = logistic(theta_samples_standard_normal)

# Create a single figure
fig, ax1 = plt.subplots(figsize=(10, 8))

# Plot the logistic function and density of theta on the primary x-axis
ax1.plot(theta_range, eta_values, label='Logistic Function', color='blue', linewidth=2)
sns.histplot(theta_samples_standard_normal, label='Histogram of Theta', color='orange', kde=True, bins=50, ax=ax1, stat="density", alpha=0.3)
sns.kdeplot(theta_samples_standard_normal, label='Density of Theta', color='orange', linewidth=2, ax=ax1)

# Add labels and grid for the primary axis
ax1.set_title('Logistic Function and Densities of Theta and Eta', fontsize=14)
ax1.set_xlabel('Theta', fontsize=12)
ax1.set_ylabel('Density / Logistic Value', fontsize=12)
ax1.grid()
ax1.legend(loc='upper right', fontsize=12)

# Create a secondary y-axis for the density of eta
ax2 = ax1.twinx()
sns.histplot(eta_samples_standard_normal, label='Histogram of Eta', color='green', kde=True, bins=50, ax=ax2, stat="density", alpha=0.3, orientation="horizontal")
sns.kdeplot(y=eta_samples_standard_normal, label='Density of Eta', color='green', linewidth=2, ax=ax2)

# Add labels and legend for the secondary axis
ax2.set_ylabel('Density of Eta', fontsize=12, color='green')
ax2.legend(loc='upper left', fontsize=12)

plt.show()