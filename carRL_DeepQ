# This is a demo program, showing a simple version of reinforcement learning for a pre-existing environment
# Taxi must take passenger to hotel

import numpy as np
import random
import gym

env = gym.make('Taxi-v3')

alpha = 0.9  # Learning Rate
gamma = 0.95
epsilon = 1  # Exploration Rate
epsilonDecay = 0.995
minEpsilon = 0.01
numEpisodes = 10000
maxSteps = 100


qTable = np.zeros((env.observation_space.n, env.action_space.n))

def chooseAction(state):
    if random.random() < epsilon:
        return env.action_space.sample()

    else:
        return np.argmax(qTable[state, :])


for episode in range(numEpisodes):
    state, _ = env.reset()

    done = False

    for step in range(maxSteps):
        action = chooseAction(state)

        nextState, reward, done, truncated, info = env.step(action)

        oldValue = qTable[state, action]
        nextMax = np.max(qTable[nextState, :])

        qTable[state, action] = (1 - alpha) * oldValue + alpha * (reward + gamma * nextMax)

        state = nextState

        if done or truncated:
            break

    epsilon = max(epsilon * epsilonDecay, minEpsilon)

env = gym.make('Taxi-v3', render_mode='human')

for episode in range(5):
    state, _ = env.reset()
    done = False

    print("Episode", episode)

    for step in range(maxSteps):
        env.render()
        action = np.argmax(qTable[state, :])
        nextState, reward, done, truncated, _ = env.step(action)

        if done or truncated:
            env.render()
            print("Finished episode", episode, "with reward", reward)
            break

env.close()



