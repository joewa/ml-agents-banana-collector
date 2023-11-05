# ml-agents-banana-collector
Collect good food and avoid bad food using Deep Q-Networks with Gym and Unity ML-Agents Toolkit

<img src="assets/food-collector-DQN-training-unity.gif" width="70%">

This repository solves the [Banana Collector project](https://github.com/udacity/deep-reinforcement-learning/tree/561eec3ae8678a23a4557f1a15414a9b076fdfff/p1_navigation) from the Udacity "Deep Reinforcement Learning" Nanodegree. However, there are no bananas...

## Background
The [introduction video from Udacity about how DeepMind leveraged a Deep Q-Network (DQN) to build the Deep Q-Learning algorithm that learned to play many Atari video games better than humans](https://youtu.be/GgtR_d1OB-M) explains in brief the algorithms and concepts applied in this project. The naive Q-learning algorithm is enhanced by a replay buffer and uses [Experience Replay](https://www.youtube.com/watch?v=wX_-SZG-YMQ) to sample from the buffer at random. Additionally, two separate networks with identical architectures are used and the "target" Q-Networks's weights are updated less often than the "primary" Q-Network. This concept decouples the updating of the networks weights from the agent's actions, providing a more stable learning environment as explained in [this video](https://www.youtube.com/watch?v=SWpyiEezfp4). More details are provided in the paper "[Human-level control through deep reinforcement learning](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf)" from Google DeepMind.

## Extending the challenge
The pre-built Banana Collector environments as described in the [project instructions](https://github.com/udacity/deep-reinforcement-learning/tree/561eec3ae8678a23a4557f1a15414a9b076fdfff/p1_navigation) could not be used for solving the challenge. Instead, [ML-Agent's Food Collector learning environment](https://github.com/Unity-Technologies/ml-agents/blob/7a03145ae48ad354821bd89e0243d99332149ace/docs/Learning-Environment-Examples.md#food-collector) was adapted to mimic the behaviour of the Banana Collector. So Udacity's great lectures and the example will remain useful even though ML-Agents and Unity evolves. Furthermore, understanding end to end the DQN's theory and how Unity and ML-Agents work certainly provide an inspiring experience.

## Summary of the solution
This repository contains the complete source code to reproduce the presented results. The Unity ML-Agents's environment contains three sensors, but only one at a time is used for training and inference.
- [Ray Perception Sensor 3D](https://www.immersivelimit.com/tutorials/rayperceptionsensorcomponent-tutorial) with 6 Rays Per Direction and 3 Stacked Raycasts.
- [Camera Sensor](https://www.youtube.com/watch?v=7FHyqzUBzZ0), mounted at the agent (40x40 RGB).
- Grid Sensor, used for observing the training progress only.

The [example solution of the LunarLander Gym environment](https://github.com/udacity/deep-reinforcement-learning/blob/561eec3ae8678a23a4557f1a15414a9b076fdfff/dqn/solution/Deep_Q_Network_Solution.ipynb) was adapted for solving the Banana Collector.
- For the Ray Perception sensor, the QNetwork with three fully connected linear layers and ReLu activation functions was adapted to the dimension of the observation and the action space only and performed very good.
- For the Camera sensor, two network architectures were tested
    - 3 layer CNN with 5x5 kernels, inspired by [this solution](https://github.com/tjwhitaker/human-level-control-through-deep-reinforcement-learning/blob/241901bd8baa7dc18b596795ebcef9e21adcd4eb/src/model.py) based on the DeepMind paper. It achieved ~50% of the score of the Ray Perception Sensor baseline.
    - 2 layer CNN with a 9x9 kernel and 4x4 max pooling followed by a 5x5 kernel and a 2x2 max pooling followed by 3 fully connected layers performed much better and achieved ~75% of the score of the Ray Perception Sensor baseline.

TODO: another short demo video here.

The **complete code and the detailed results are provided in the notebook and the report**.

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
