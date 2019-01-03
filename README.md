# IMBandits

IMBandit.py -- Simulator.

egreedy.py -- epsilon-greedy and UCB1 exploration strategy.

degreeDiscount.py, generalGreedy.py -- Two different oracles (IM algorithm).

IC/IC.py -- Independent cascade model, runIC() returns influence result given seed nodes.

### Result

#### Parameter

```python
graph_address = './datasets/Flickr/Small_Final_SubG.G'
prob_address = './datasets/Flickr/Probability.dic'

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
```

#### Experiment

```
Dimension: 4, Node number:6191, Edge Number: 9288
average reward for oracle: 252.19
UCB1: 96.94
egreedy_0.1: 160.16
OurAlgorithm: 223.68
```
<p float="left">
<img src="./SimulationResults/avgReward-normal.png" alt="alt text" width="400" height="300">
<img src="./SimulationResults/acuReward-normal.png" alt="alt text" width="400" height="300">
</p>

```
Dimension: 4, Node number:13353, Edge Number: 131534
average reward for oracle: 6204.25
UCB1: 6217.24
egreedy_0.1: 6215.47
OurAlgorithm: 6213.86
```



<p float="left">
<img src="./SimulationResults/avgReward-dense.png" alt="alt text" width="400" height="300">
<img src="./SimulationResults/acuReward-dense.png" alt="alt text" width="400" height="300">
</p>





```
Dimension: 4, Node number:13353, Edge number: 131534
average reward for oracle: 532.15
UCB1: 437.42
egreedy_0.1: 493.68
OurAlgorithm: 470.27
```

<p float="left">
<img src="./SimulationResults/avgReward-denseLowProb.png" alt="alt text" width="400" height="300">
<img src="./SimulationResults/acuReward-denseLowProb.png" alt="alt text" width="400" height="300">
</p>



Loss for Dimension 1, Dimension 4, Dimension 16:

<p float="left">
<img src="./SimulationResults/Loss-1.png" alt="alt text" width="260" height="200">
<img src="./SimulationResults/Loss-4.png" alt="alt text" width="260" height="200">
<img src="./SimulationResults/Loss-16.png" alt="alt text" width="260" height="200">
</p>