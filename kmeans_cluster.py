from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
X,y=load_iris(return_X_y=True)
Kmeans=KMeans(n_clusters=3)
Kmeans.fit(X)
print(Kmeans.labels_)
