import os
from Oracle.generalGreedy import generalGreedy
from Oracle.degreeDiscount import degreeDiscountIC, degreeDiscountIC2, degreeDiscountIAC, degreeDiscountIAC2, degreeDiscountStar, degreeDiscountIAC3

save_address = "./SimulationResults"

graph_address = './datasets/Flickr/Small_Final_SubG.G'
prob_address = './datasets/Flickr/Probability.dic'
param_address = './datasets/Flickr/Small_nodeFeatures.dic'

dataset = 'Flickr' #Choose from 'default', 'NetHEPT', 'Flickr'
batchSize = 1
alpha_1 = 0.2
alpha_2 = 0.2 
lambda_ = 0.4
gamma = 0.1
dimension = 4
seed_size = 40
iterations = 200

oracle = degreeDiscountIAC3
