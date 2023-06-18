# K-Means Clustering - Custom Implementation

This repository contains a Python implementation of the K-Means clustering algorithm. The purpose of this project is to understand the underlying logic and functioning of the K-Means algorithm without relying on existing machine learning libraries. The code reads in a dataset and performs K-Means clustering on it, providing a quality measure for the resulting clusters.

## Dependencies

The following Python libraries are required to run the script:

- pandas
- numpy
- random
- copy
- scipy

### Usage

To run the script, simply use Python 3 as follows:

``` python kmeans_jovanailin.py ```

Before running the script, make sure to set the attribute weights and the number of clusters (k) as per your requirements in the `kmeans_jovanailin.py` file.

### Algorithm

The K-Means algorithm implemented in this script involves the following steps:

1. **Random centroid initialization**: Random values within the data range are selected as the initial centroids of the clusters.
2. **Distance calculation**: The Euclidean or City Block distance between each data point and the centroids is calculated.
3. **Assignment of points to clusters**: Each data point is assigned to the cluster whose centroid it is closest to.
4. **Centroid update**: The centroids of the clusters are updated based on the mean of the data points assigned to the cluster.
5. **Convergence check**: If the centroids have stopped changing, the algorithm stops. If they haven't, steps 2-4 are repeated.
6. **Quality of clustering**: The quality of the clusters is calculated based on the sum of the distances between the data points and their assigned centroids. The lower the quality measure (q), the better the clustering.
7. **Multiple runs**: The entire process is run multiple times, and the clustering with the best quality is selected as the final output.

#### Learning Objectives
The purpose of this project is to understand the underlying workings of the K-Means clustering algorithm without using any existing machine learning libraries. This will enable you to gain a deeper understanding of how the K-Means algorithm works in practice and how it can be applied to real-world datasets.

Enjoy exploring the world of unsupervised learning with this barebones K-Means clustering implementation!

