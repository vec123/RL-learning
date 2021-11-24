#Define Environment
import gym
from gym import spaces
import numpy as np

class SineEnv(gym.Env):
  #"""Custom Environment that follows gym interface"""
  #metadata = {'render.modes': ['human']}

  def __init__(self,  num_actions=1, num_states=2, lower_action_bound = -1 , higher_action_bound = 1):
    super(SineEnv, self).__init__(  )

    self.val = 0
    self.reward = 0
    self.episode_lenght = 100
    self.current_step = 0

    #Define action and observation space
    #They must be gym.spaces objects
    #actions we can take: down, stay, up
    #self.action_space = spaces.Discrete(3)
    #actions we can take: numerical value between action_bound
    self.action_space = spaces.Box(low=lower_action_bound, high=higher_action_bound, shape=(num_actions,))
    # Example for using image as input:
    #self.observation_space = spaces.Discrete(0)
    #1-D number
    self.observation_space = spaces.Box(low=0, high=255, shape=(num_states,))
#                    (HEIGHT, WIDTH, N_CHANNELS), dtype=np.uint8)


  def step(self, action, sine_value):
    # Execute one time step within the environment
    self.current_step += 1

    obs = sine_value
    self.val =  self.val + action


    if obs != self.val:
        self.reward = 1/np.power((obs - self.val),2)
    elif obs == self.val:   #avoid singularity
        print("val == obs")
        self.reward = 10000
    else:
        print("this should never be printed 1")

    if self.current_step >= self.episode_lenght:
        done = True
    elif self.current_step < self.episode_lenght:
        done = False
    else:
        print("this should never be printed 2")

    info = done

    return obs, self.val, self.reward, done, info

  def reset(self):
    # Reset the state of the environment to an initial state
    self.state = (0,0)
    self.current_step = 0
    self.reward = 0
    return  np.array(self.state)

  def render(self, mode='human', close=False):
    print(self.reward)
