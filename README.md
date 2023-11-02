# ml-agents-banana-collector
Collect good food and avoid bad food using Deep Q-Networks with Gym and Unity ML-Agents Toolkit

This repository solves the [Banana Collector project](https://github.com/udacity/deep-reinforcement-learning/tree/561eec3ae8678a23a4557f1a15414a9b076fdfff/p1_navigation) from the Udacity "Deep Reinforcement Learning" Nanodegree. However, there are no bananas...

## Extending the challenge
The pre-built Banana Collector environments as described in the [project instructions](https://github.com/udacity/deep-reinforcement-learning/tree/561eec3ae8678a23a4557f1a15414a9b076fdfff/p1_navigation) could not be used for solving the challenge. Instead, [ML-Agent's Food Collector learning environment](https://github.com/Unity-Technologies/ml-agents/blob/7a03145ae48ad354821bd89e0243d99332149ace/docs/Learning-Environment-Examples.md#food-collector) was adapted to mimic the behaviour of the Banana Collector. So Udacity's great lectures and the example will remain useful even though ML-Agents and Unity evolves. Furthermore, understanding end to end the DQN's theory and how Unity and ML-Agents work certainly provide an inspiring experience.

## Installation and setting up the environment
Clone the current repository using
```
git clone https://github.com/joewa/ml-agents-banana-collector.git
```
Following [ML-Agents's installation instructions](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Installation.md) is recommended to get an up-to-date environment. 

Of course, replicating the current environment at the time of writing is possible using
```
conda create --name banana --file requirements.txt
```
However, please feel encouraged to create your own up to date environment from scratch.
