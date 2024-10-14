#author: peter alonzi
#date: 2024-07-23
#description: k-means clustering

import numpy as np
import matplotlib.pyplot as plt
import subprocess
import sys
import site
from sklearn.metrics.pairwise import euclidean_distances
import matplotlib.gridspec as gridspec

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])
    site.main()  # Refresh sys.path

try:
    from sklearn.cluster import KMeans
    from sklearn.datasets import make_blobs
except ImportError:
    print("sklearn not found. Installing...")
    install("scikit-learn")
    from sklearn.cluster import KMeans
    from sklearn.datasets import make_blobs


# Generate synthetic data
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Initialize KMeans
kmeans = KMeans(n_clusters=4, random_state=0)

# Fit the model
kmeans.fit(X)

# Get cluster centers and labels
centers = kmeans.cluster_centers_

# Compute Euclidean distances between centers
distances = euclidean_distances(centers)

# Create a figure with a grid layout
fig = plt.figure(figsize=(20, 10))  # Increased figure size
gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1])

# Main scatter plot
ax1 = plt.subplot(gs[0])
scatter = ax1.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, s=70, cmap='viridis', alpha=0.7)
centers_plot = ax1.scatter(centers[:, 0], centers[:, 1], c='blue', s=250, alpha=0.8, marker='s', label='Cluster Centers')

# Find the leftmost triangle
leftmost_centers = centers[centers[:, 0].argsort()][:3]

# Shade the leftmost triangle
triangle = plt.Polygon(leftmost_centers, alpha=0.33, fill=True, edgecolor=None)
ax1.add_patch(triangle)

# Connect centers with dashed lines and label with distances
for i in range(len(centers)):
    for j in range(i+1, len(centers)):
        line = ax1.plot([centers[i, 0], centers[j, 0]], [centers[i, 1], centers[j, 1]], 'b--', alpha=0.5)[0]
        
        # Calculate midpoint for label positioning
        midpoint = ((centers[i, 0] + centers[j, 0]) / 2, (centers[i, 1] + centers[j, 1]) / 2)
        
        # Calculate distance
        distance = np.linalg.norm(centers[i] - centers[j])
        
        # Add label
        ax1.annotate(f'{distance:.2f}', xy=midpoint, xytext=(0, 3), 
                     textcoords='offset points', ha='center', va='bottom',
                     bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.7),
                     fontsize=8)

ax1.set_title('K-means Clustering Result', fontsize=18, fontweight='bold')
ax1.set_xlabel('Feature 1', fontsize=14, fontweight='bold')
ax1.set_ylabel('Feature 2', fontsize=14, fontweight='bold')

# Add grid lines
ax1.grid(True, linestyle='--', alpha=0.7)

# Add tick marks and make them more visible
ax1.tick_params(axis='both', which='major', labelsize=12, width=1, length=6)
ax1.tick_params(axis='both', which='minor', labelsize=10, width=1, length=4)

# Add legend
legend1 = ax1.legend(*scatter.legend_elements(), title="Clusters", loc="upper right", fontsize=12)
ax1.add_artist(legend1)
ax1.legend(handles=[centers_plot], loc='upper left', fontsize=12)

# Add center coordinates as text
for i, center in enumerate(centers):
    ax1.annotate(f'Center {i+1}: ({center[0]:.2f}, {center[1]:.2f})',
                 xy=(1.02, 0.95 - i*0.06), xycoords='axes fraction',
                 fontsize=12, ha='left', va='center')

# Distance matrix plot
ax2 = plt.subplot(gs[1])
im = ax2.imshow(distances, cmap='YlOrRd')  # Changed colormap for better contrast
ax2.set_title('Euclidean Distances\nBetween Centers', fontsize=18, fontweight='bold')
ax2.set_xlabel('Center', fontsize=14, fontweight='bold')
ax2.set_ylabel('Center', fontsize=14, fontweight='bold')

# Add tick marks and make them more visible
ax2.tick_params(axis='both', which='major', labelsize=12, width=1, length=6)
ax2.set_xticks(range(len(centers)))
ax2.set_yticks(range(len(centers)))

# Add colorbar
cbar = plt.colorbar(im, ax=ax2)
cbar.set_label('Distance', fontsize=14, fontweight='bold')
cbar.ax.tick_params(labelsize=12)

# Add distance values in the cells
for i in range(len(centers)):
    for j in range(len(centers)):
        ax2.text(j, i, f'{distances[i, j]:.2f}', 
                 ha='center', va='center', color='black', fontweight='bold', fontsize=10)

plt.tight_layout()  # Adjust layout to prevent clipping of annotations
plt.show()




