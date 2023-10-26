import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load your data (assuming you have a CSV file, modify the path accordingly)
data = pd.read_csv("customer_data.csv")

# Assuming you have columns 'Age' and 'Income' for segmentation
# Select the features for clustering
features = data[['Age', 'Income']]

# Standardize the features (important for K-Means)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Determine the optimal number of clusters using the Elbow Method
#inertia = []
#for i in range(1, 11):
#    kmeans = KMeans(n_clusters=i, random_state=42)
#    kmeans.fit(scaled_features)
#    inertia.append(kmeans.inertia_)

# Plot the Elbow graph to find the optimal number of clusters
#plt.figure(figsize=(8, 6))
#plt.plot(range(1, 11), inertia, marker='o', linestyle='--')
#plt.xlabel('Number of Clusters')
#plt.ylabel('Inertia')
#plt.title('Elbow Method for Optimal K')
#plt.show()

# Based on the elbow method, choose the optimal number of clusters (let's say 3 in this case)
optimal_clusters = 3

# Perform K-Means clustering
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(scaled_features)

# Add cluster labels to the original data
data['Cluster'] = cluster_labels

# Print and analyze the clusters
for cluster in range(optimal_clusters):
    print(f"Cluster {cluster}:")
    print(data[data['Cluster'] == cluster][['Age', 'Income']])
    print("--------------------------")

