import sys
import gym
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from DDPG_agent import DDPGagent
from utils import *
from environment import SineEnv
import csv


lower_action_bound = -1
higher_action_bound = 1
num_states = 2
num_actions = 1
amplitude = 1
frequency = 0.005
episode_duration = 501

#env = NormalizedEnv(gym.make("Pendulum-v0"))
#env = gym.make("Pendulum-v0")
env = SineEnv(amplitude, frequency, episode_duration, num_actions=num_actions, num_states=num_states, lower_action_bound = lower_action_bound , higher_action_bound = higher_action_bound )
#env2 = NormalizedEnv(env)


agent = DDPGagent(env)
noise = OUNoise(env.action_space)
batch_size = 128
rewards = []
avg_rewards = []
actions_all = []
states_all = []
sines_all = []
rewards_all = []
for episode in range(5):
    print(episode)
    if episode != 0:
        print(episode_reward)
    state = env.reset()
    noise.reset()
    episode_reward = 0
    actions_l = []
    states_l = []
    sines_l = []
    reward_l = []
    done = False
    step =0
    while step in range(500) and done == False:
        action = agent.get_action(state)
        action = noise.get_action(action, step)
        new_state, reward, done, _ = env.step(action)
        agent.memory.push(state, action, reward, new_state, done)
        if len(agent.memory) > batch_size:
            agent.update(batch_size)
        state = new_state
        episode_reward += reward
        reward_l.append(reward)
        actions_l.append(action)
        states_l.append(state)
        step += step
        if done:
            sys.stdout.write("episode: {}, reward: {}, average _reward: {} \n".format(episode, np.round(episode_reward, decimals=2), np.mean(rewards[-10:])))
            break
    actions_all.append(actions_l)
    states_all.append(states_l)
    rewards_all.append(reward_l)
    rewards.append(episode_reward)
    avg_rewards.append(np.mean(rewards[-10:]))



with open("actions_all.csv", "w", newline='') as f:
    wr = csv.writer(f)
    wr.writerows( map (list, zip(*actions_all) ) )
with open("actions_all_rows.csv", "w", newline='') as f:
    wr = csv.writer(f)
    wr.writerows( actions_all)

with open("states_all.csv", "w", newline='') as f:
    wr = csv.writer(f)
    wr.writerows(map (list, zip(*states_all) ) )
with open("rewards_all.csv", "w", newline='') as f:
    wr = csv.writer(f)
    wr.writerows(map (list, zip(*rewards_all) ) )
with open("sines_all.csv", "w", newline='') as f:
    wr = csv.writer(f)
    wr.writerows(map (list, zip(*sines_all) ) )

plt.figure()
plt.plot(actions_all[0])
plt.plot()
plt.xlabel('Episode 10')
plt.ylabel('Actions')
plt.savefig("actions")

plt.figure()
plt.plot(states_all[0])
plt.plot()
plt.xlabel('Episode 10')
plt.ylabel('States')
plt.savefig("states")

plt.figure()
plt.plot(rewards)
plt.plot(avg_rewards)
plt.plot()
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.savefig("reward")
