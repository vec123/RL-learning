#Define Environment
import gym
from gym import spaces
import numpy as np
import csv
import math

class SineEnv(gym.Env):
  #"""Custom Environment that follows gym interface"""
  #metadata = {'render.modes': ['human']}

  def __init__(self, amplitude, frequency, episode_len,  num_actions=2, num_states=2, lower_action_bound = -1 , higher_action_bound = 1):
    super(SineEnv, self).__init__(  )


    self.state = np.array([0,0])
    self.obs = 0
    self.reward = 0
    self.episode_duration = episode_len
    self.w = 2. * math.pi * frequency
    self.t = np.linspace(0, self.episode_duration, self.episode_duration)
    self.sine=np.sin(self.w *self.t)*amplitude
    np.savetxt("sine_from_env.csv",self.sine)
    self.current_t = 0
    self.amplitude = amplitude

    self.action_space = spaces.Box(low=lower_action_bound, high=higher_action_bound, shape=(num_actions,))
    self.observation_space = spaces.Box(low=0, high=255, shape=(num_states,))


  def step(self, action):
    # Execute one time step within the environment
    done = False
    self.current_t += 1
    obs_old = self.obs
    self.obs = float(action)


    if self.current_t != 0:
        old_reward=self.reward

    if self.obs != self.sine[self.current_t-1]:
         self.reward = - 3*np.absolute(self.obs - self.sine[self.current_t-1]) + self.current_t #np.power(1.1,self.current_t)

    elif self.obs == self.sine[self.current_t-1]:

        self.reward = 10000000000000

    if self.current_t >= self.episode_duration:
        done = True
    elif self.current_t < self.episode_duration:
        done = False
    else:
        print("this should never be printed 2")

    if  np.absolute(self.obs - self.sine[self.current_t-1]) > 1.4:
        self.reward = -10000000000000
        done = True

    info = done

    self.state = np.array([self.obs,obs_old])
    return self.state, self.reward, done, info

  def reset(self):
    # Reset the state of the environment to an initial state
    self.state = np.array([0,0])
    self.current_t = 0
    self.reward = 0
    return  np.array(self.state)

  def render(self, mode='human', close=False):
    print(self.reward)
