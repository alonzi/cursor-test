import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Create points for x-axis
x = np.linspace(-5, 5, 1000)

# Calculate the standard normal distribution
y = norm.pdf(x, 0, 1)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(x, y, 'b-', lw=2, label='Standard Normal Distribution')

# Fill areas for different sigma regions
plt.fill_between(x, y, where=(x >= -1) & (x <= 1), color='red', alpha=0.2, 
                label='±1σ (68.27%)')
plt.fill_between(x, y, where=(x >= -2) & (x <= 2), color='yellow', alpha=0.1, 
                label='±2σ (95.45%)')
plt.fill_between(x, y, where=(x >= -3) & (x <= 3), color='green', alpha=0.1, 
                label='±3σ (99.73%)')

# Add vertical lines for sigma values
for sigma in [-3, -2, -1, 0, 1, 2, 3]:
    plt.axvline(x=sigma, color='gray', linestyle='--', alpha=0.5)
    plt.text(sigma, -0.02, f'{sigma}σ', horizontalalignment='center')

# Add real-world probability annotations with larger, bold text and emojis
# Car accident: ~1 in 366 per year
car_sigma = norm.ppf(1/366)
plt.annotate(f'🚗 Car accident (1 in 366)\n{car_sigma:.2f}σ', 
            xy=(car_sigma, norm.pdf(car_sigma, 0, 1)),
            xytext=(car_sigma+2, 0.3),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12,
            weight='bold')

# Lightning strike: ~1 in 500,000 per year
lightning_sigma = norm.ppf(1/500000)
plt.annotate(f'⚡ Lightning strike (1 in 500k)\n{lightning_sigma:.2f}σ', 
            xy=(lightning_sigma, norm.pdf(lightning_sigma, 0, 1)),
            xytext=(lightning_sigma+2.5, 0.2),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12,
            weight='bold')

# Airplane accident: ~1 in 11 million per year
plane_sigma = norm.ppf(1/11000000)
plt.annotate(f'✈️ Plane accident (1 in 11M)\n{plane_sigma:.2f}σ', 
            xy=(plane_sigma, norm.pdf(plane_sigma, 0, 1)),
            xytext=(plane_sigma+3, 0.1),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12,
            weight='bold')

# Customize the plot
plt.title('Standard Normal Distribution with Annual Risk Comparisons', fontsize=14)
plt.xlabel('Standard Deviations (σ)', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

# Add text box with probabilities
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textstr = '\n'.join([
    'Probabilities:',
    '±1σ: 68.27%',
    '±2σ: 95.45%',
    '±3σ: 99.73%',
    '±4σ: 99.994%',
    '±5σ: 99.99994%'
])
plt.text(3.5, 0.35, textstr, bbox=props)

plt.show()
