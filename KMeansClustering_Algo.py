import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.cluster import KMeans
style.use('ggplot')

df = pd.read_excel('data.xlsx',index=0)
print(df.head())


Z = np.array([[1,2],
              [1.5,1.8],
              [5,8],
              [8,8],
              [1,0.6],
              [9,11]])

X = df
print(X)

clf = KMeans(n_clusters = 2)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_

#print(centroids,labels)

colors = 10*["g.","r.","c.","b.","k."]

for i in range(len(X)):
    plt.plot(X[i][0],X[i][1], colors[labels[i]],markersize=25)

plt.scatter(centroids[:,0],centroids[:,1],marker='x')
plt.show()
