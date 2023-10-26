from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

iris_data = load_iris()  # Loading iris dataset from sklearn.datasets
iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)  # Creating DataFrame

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=100, n_init=10, random_state=0)  # Applying KMeans classifier
y_kmeans = kmeans.fit_predict(iris_df)

print(kmeans.cluster_centers_)  # Display cluster centers

plt.scatter(iris_df.iloc[y_kmeans == 0, 0], iris_df.iloc[y_kmeans == 0, 1], s=100, c='red', label='Iris-setosa')
plt.scatter(iris_df.iloc[y_kmeans == 1, 0], iris_df.iloc[y_kmeans == 1, 1], s=100, c='blue', label='Iris-versicolour')
plt.scatter(iris_df.iloc[y_kmeans == 2, 0], iris_df.iloc[y_kmeans == 2, 1], s=100, c='green', label='Iris-virginica')  # Visualizing the clusters - On the first two columns
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='black', label='Centroids')  # Plotting the centroids of the clusters
plt.legend()
plt.show()

