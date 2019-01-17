# IMBandits

IMBandit.py -- Simulator.

egreedy.py -- epsilon-greedy and UCB1 exploration strategy.

degreeDiscount.py, generalGreedy.py -- Two different oracles (IM algorithm).

IC/IC.py -- Independent cascade model, runIC() returns influence result given seed nodes.

### Result

Simulation dimension: 20

<p float="left">
<img src="./SimulationResults/ModelMismatch.png" alt="alt text" width="400" height="300">
</p>

#### Parameter

```python
graph_address = './datasets/Flickr/Small_Final_SubG.G'
prob_address = './datasets/Flickr/Probability.dic'

dataset = 'Flickr' #Choose from 'default', 'NetHEPT', 'Flickr'
batchSize = 1
alpha_1 = 0.1
alpha_2 = 0.1 
lambda_ = 0.4
gamma = 0.1
dimension = 4
seed_size = 300
iterations = 200

oracle = degreeDiscountIAC3
```

#### Experiment

```
average reward for oracle: 1144.06
UCB1: 855.26
egreedy_0.1: 1033.51
OurAlgorithm: 1057.44
```
<p float="left">
<img src="./SimulationResults/avgReward-dense.png" alt="alt text" width="400" height="300">
<img src="./SimulationResults/acuReward-dense.png" alt="alt text" width="400" height="300">
</p>

```
average reward for oracle: 1075.605
UCB1: 447.38
egreedy_0.1: 873.09
OurAlgorithm: 971.12
```

<p float="left">
<img src="./SimulationResults/avgReward-cluster.png" alt="alt text" width="400" height="300">
<img src="./SimulationResults/acuReward-cluster.png" alt="alt text" width="400" height="300">
</p>

