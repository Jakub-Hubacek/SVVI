import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.utils import shuffle

dataset = pd.read_csv("cvicenie5\Mall_Customers.csv")
X = dataset.iloc[:, [3, 4]].values  # Vyberáme stĺpce 'Annual Income' a 'Spending Score'


def run_kmeans(X, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, init="k-means++", random_state=42)
    y_kmeans = kmeans.fit_predict(X)
    return kmeans, y_kmeans


def plot_clusters(X, y_kmeans, kmeans, n_clusters):
    colors = ["red", "blue", "green", "cyan", "magenta", "black"]
    for i in range(n_clusters):
        plt.scatter(
            X[y_kmeans == i, 0],
            X[y_kmeans == i, 1],
            s=100,
            c=colors[i],
            label=f"Cluster {i + 1}",
        )
    plt.scatter(
        kmeans.cluster_centers_[:, 0],
        kmeans.cluster_centers_[:, 1],
        s=300,
        c="yellow",
        label="Centroids",
    )
    plt.title(f"Clusters of customers (n_clusters = {n_clusters})")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    plt.legend()
    plt.show()


subsets = [0.2, 0.5, 0.75]
for subset in subsets:
    # Náhodne premiešame dataset
    X_shuffled = shuffle(X, random_state=42)

    subset_size = int(len(X_shuffled) * subset)
    X_subset = X_shuffled[:subset_size]

    # Použitie elbow metódy na nájdenie optimálneho počtu klastrov
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
        kmeans.fit(X_subset)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1, 11), wcss)
    plt.title(f"The Elbow Method (subset = {int(subset * 100)}%)")
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.show()

   
    n_clusters = 5
    if subset == 0.2:
        n_clusters = 5
    elif subset == 0.5:
        n_clusters = 6
    elif subset == 0.75:
        n_clusters = 5
    kmeans, y_kmeans = run_kmeans(X_subset, n_clusters)
    plot_clusters(X_subset, y_kmeans, kmeans, n_clusters)
