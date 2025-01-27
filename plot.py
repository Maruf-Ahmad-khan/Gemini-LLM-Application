import numpy as np
import matplotlib.pyplot as plt

class Gaussian:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def pdf(self, x):
        """Probability Density Function"""
        return (1 / (self.sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - self.mu) / self.sigma)**2)

# Example usage:
mu = 0  # Mean
sigma = 1 # Standard Deviation

gaussian = Gaussian(mu, sigma)

# Generate x values for plotting
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)  # 3 standard deviations on either side

# Calculate y values (PDF)
y = gaussian.pdf(x)

# Plotting
plt.plot(x, y)
plt.title('Gaussian Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()