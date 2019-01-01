import random
import heapq
import datetime
import networkx as nx
import math
import argparse
import matplotlib.pyplot as plt
import time
import pickle
import numpy as np
import operator

save_dir = '../datasets/Flickr/'
def featureUniform(dimension, scale=1):
	vector = np.array([random.random() for i in range(dimension)])
	l2_norm = np.linalg.norm(vector, ord =2)
	
	vector = vector/l2_norm
	if random.random()<0.3:
		vector = vector*0.3
	vector = vector * scale
	return vector

dimension = 4
nodeDic = {}
edgeDic = {}
G = pickle.load(open(save_dir+'Small_Final_SubG.G', 'rb'))
for u in G.nodes():
	nodeDic[u] = [featureUniform(dimension), featureUniform(dimension)]
for u in G.nodes():
	for v in G[u]:
		edgeDic[(u,v)] = np.dot(nodeDic[u][1], nodeDic[v][0])

pickle.dump(nodeDic, open(save_dir+'Small_nodeFeatures.dic', "wb" ))
pickle.dump(edgeDic, open(save_dir+'Probability.dic', "wb" ))