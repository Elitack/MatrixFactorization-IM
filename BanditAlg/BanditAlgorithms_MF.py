import numpy as np
import networkx as nx
from BanditAlg.BanditAlgorithms import ArmBaseStruct
from conf import *
import random

class MFUserStruct:
	def __init__(self, featureDimension, lambda_, userID):
		self.userID = userID
		self.dim = featureDimension
		self.A = lambda_*np.identity(n = self.dim)
		self.C = lambda_*np.identity(n = self.dim)

		self.b = np.array([random.random() for i in range(self.dim)])
		self.d = np.array([random.random() for i in range(self.dim)])
		self.AInv = np.linalg.inv(self.A)
		self.CInv = np.linalg.inv(self.C)

		self.theta_out = np.dot(self.AInv, self.b)
		self.theta_in = np.dot(self.CInv, self.d)

		self.pta_max = 1
		
	def updateOut(self, articlePicked_FeatureVector, click):
		self.A += np.outer(articlePicked_FeatureVector,articlePicked_FeatureVector)
		self.b += articlePicked_FeatureVector*click
		self.AInv =  np.linalg.inv(self.A)
		self.theta_out = np.dot(self.AInv, self.b)

	def updateIn(self, articlePicked_FeatureVector, click):
		self.C += np.outer(articlePicked_FeatureVector,articlePicked_FeatureVector)
		self.d += articlePicked_FeatureVector*click
		self.CInv =  np.linalg.inv(self.C)
		self.theta_in = np.dot(self.CInv, self.d)

class MFAlgorithm:
	def __init__(self, G, seed_size, oracle, dimension, feedback = 'edge'):
		self.G = G
		self.oracle = oracle
		self.seed_size = seed_size

		self.dimension = dimension
		self.feedback = feedback

		self.currentP =nx.DiGraph()
		self.users = {}  #Nodes
		for u in self.G.nodes():
			self.users[u] = MFUserStruct(dimension, lambda_ , u)
			for v in self.G[u]:
				self.currentP.add_edge(u,v, weight=random.random())

	def decide(self):
		S = self.oracle(self.G, self.seed_size, self.currentP)
		return S

	def updateParameters(self, S, live_nodes, live_edges):
		for u in live_nodes:
			for (u, v) in self.G.edges(u):
				if (u,v) in live_edges:
					reward = live_edges[(u,v)]
				else:
					reward = 0
				self.users[u].updateOut(self.users[v].theta_in, reward)
				self.users[v].updateIn(self.users[u].theta_out, reward)
				self.currentP[u][v]['weight']  = self.getP(self.users[u], self.users[v])

	def getP(self, u, v):
		CB = alpha_1 * np.dot(np.dot(v.theta_in, u.AInv), v.theta_in) + alpha_2 * np.dot(np.dot(u.theta_out, v.CInv), u.theta_out)
		prob = np.dot(u.theta_out, v.theta_in) + CB
		if prob > 1:
			prob = 1
		if prob < 0:
			prob = 0
		return prob		
