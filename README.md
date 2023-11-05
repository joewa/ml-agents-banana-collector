# ml-agents-banana-collector
Collect good food and avoid bad food using Deep Q-Networks with Gym and Unity ML-Agents Toolkit

![Training DQN agent with Unity and ML-Agent's](assets/food-collector-DQN-training-unity.gif)

This repository solves the [Banana Collector project](https://github.com/udacity/deep-reinforcement-learning/tree/561eec3ae8678a23a4557f1a15414a9b076fdfff/p1_navigation) from the Udacity "Deep Reinforcement Learning" Nanodegree. However, there are no bananas...

## Background
The [introduction video from Udacity about how DeepMind leveraged a Deep Q-Network (DQN) to build the Deep Q-Learning algorithm that learned to play many Atari video games better than humans](https://youtu.be/GgtR_d1OB-M) explains in brief the algorithms and concepts applied in this project. The naive Q-learning algorithm is enhanced by a replay buffer and uses [Experience Replay](https://www.youtube.com/watch?v=wX_-SZG-YMQ) to sample from the buffer at random. Additionally, two separate networks with identical architectures are used and the "target" Q-Networks's weights are updated less often than the "primary" Q-Network. This concept decouples the updating of the networks weights from the agent's actions, providing a more stable learning environment as explained in [this video](https://www.youtube.com/watch?v=SWpyiEezfp4). More details are provided in the paper "[Human-level control through deep reinforcement learning](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf)" from Google DeepMind.

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
