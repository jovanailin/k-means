# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:05:38 2020

@author: Jovana
"""
import pandas as pd
import numpy as np
import random
import copy
from scipy.spatial.distance import cdist
np.set_printoptions(formatter={'float_kind':lambda x: "%.3f" % x})
pd.set_option('chop_threshold',0.01)

data = pd.read_csv('boston.csv')
weights=[100,50,1,50,100,100,50,100,1,1,1,50,100,100] #tezine atributa, unosi ih korisnik


data = data.multiply(weights,axis=1) #svaki red se mnozi sa tezinama



k = 3 #broj klastera
m,n = data.shape
#n broj argumenata
#m broj slucajeva

data_mean = data.mean()/sum(weights)

data_std = data.std()

data = (data-data_mean)/data_std #normalizovanje data-e

print(n)



maxx = data.max()
minn = data.min()

def randomize(minn,maxx,n):
    vektor=[]
    for i in range(n):
        vektor.append(random.uniform(minn[i],maxx[i]))
    return vektor

def generate_centroids(): #random initialization
    centroids = []
    for i in range(k):
        centroids.append(randomize(minn,maxx,n))
    return centroids

def farthest_points(matrix): #farthest points initialization
    centroids = []
    centroids.append(matrix[0])
    for i in range(k-1):
        dist = matrix - centroids[i]
        dist = dist**2
        dist = dist.sum(axis=1)
        dist = dist**(1/2)
        argmax = dist.argmax()
        centroids.append(matrix[argmax])
    return centroids

matrix = data.as_matrix()
cen = generate_centroids()
#print("prvi red u x")
#print(matrix[0])
#print("centroidi")
#print(cen)
#print("distanca")
d = matrix[0]-cen
d = d**2
d = d.sum(axis=1)
print(d)

converged = False
current_iter = 0
max_iter = 100
niz = []
quality_of_clusters=[]
clusters=[]
N=10
for s in range(N):
  q=0  
  converged=False
  current_iter=0
  centroids = generate_centroids()  
  while not converged and current_iter<max_iter:
    
    old_centroids = copy.deepcopy(centroids)
    def distance(x,c): #Euklidska distanca
        dist = x-c #matrica koja sazdrzi k vektora
        dist = dist**2 #kvadrirane vrednosti gornje matrice
        dist = dist.sum(axis=1) #sabiranje redova
        dist = dist**(1/2) #korenovanje zbira
        return dist
    
    def city_block(x,c): #City Block distanca
        dist = x-c
        dist = abs(dist)
        dist = dist.sum(axis=1)
        return dist

    niz_indexa = []

    
    for x in matrix:
        dist = []
        dist.append(distance(x,centroids))
        
        dist=np.array(dist)
        argmin = dist.argmin()
        q=q+distance(x,centroids).sum() #racunanje kvaliteta klastera, sto je manji q to je veci kvalitet
        niz_indexa.append(argmin)

    new_matrix = [[] for i in range(len(centroids))]
    print(new_matrix)

    for i in range(k):
        subset = []
        for j in range(m):
            if niz_indexa[j]==i:
                subset.append(matrix[j])
        new_matrix[i]=subset
    
    def update_centroids(j):
        for i in range(n):
            sum=0
            for x in new_matrix[j]:
                sum = sum + x[i]
            sum = sum/len(new_matrix[j])
            centroids[j][i]=sum

    for j in range(k):
        if len(new_matrix[j])!=0:
            update_centroids(j)
        
    
    new_centroids=copy.deepcopy(centroids)
    niz = copy.deepcopy(niz_indexa)
    
    if (np.array(old_centroids)-np.array(new_centroids)).sum() == 0: converged = True
    current_iter = current_iter + 1
  quality_of_clusters.append(q)
  clusters.append(centroids)
    
#print(current_iter)
#print()
#print(centroids)
#print()
#print(niz)

best_quality = min(quality_of_clusters)
indeks = quality_of_clusters.index(best_quality)
#
#print("Najbolji klaster je: ")
#print(clusters[indeks])
#print("Dobijen iz",indeks,". pokusaja")





            
            





