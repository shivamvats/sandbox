import numpy as np
import gym
from utils import getRandInRange


class GridWorldEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, cfg):
        self.cfg = cfg

        # Construct gridworld
        self.rows, self.cols = 3, 4
        self.env = np.zeros((self.rows, self.cols))
        self.env[1, 1] = 1
        self.terminal_states = [(0, 3), (1, 3)]

        # Action space
        self.actions = {
                'L' : (0, -1),
                'U' : (-1, 0),
                'R' : (0, +1),
                'D' : (+1, 0)
                }

    def step(self, a):
        """Apply action and return obs, reward, done and info"""
        s = self.state
        info = {'obs': ['env', 'state']}
        done = False
        if s in self.terminal_states:
            done = True
        else:
            self.state = self.getSuccs(self.state, a)
            print(self.state)
        reward = self.getReward(self.state)
        obs = (self.env, self.state)
        return (obs, reward, done, info)

    def reset(self):
        self.state = (np.random.randint(0, self.rows), np.random.randint(0, self.cols))
        while not self.isValid(self.state):
            self.state = (np.random.randint(0, self.rows), np.random.randint(0, self.cols))

        obs = (self.env, self.state)
        reward = 0
        done = False
        info = {'obs': ['env', 'state']}
        return (obs, reward, done, info)

    def render(self, mode='human'):
        self.env[self.state] = 5
        print(self.env)
        self.env[self.state] = 0

    def close(self):
        pass

    def shape(self):
        return self.env.shape

    def isValid(self, state):
        row, col = state
        if row >= 0 and row < self.rows and col >= 0 and col < self.cols:
            return not self.env[state]
        else:
            return False

    def getReward(self, s):
        if s == (0, 3):
            return 1
        elif s == (1, 3):
            return -1
        else:
            return 0

    def getSuccs(self, s, a):
        """Model vs model-free

        Underlying transition model: 0.8 chance that agents goes in the `a`
        direction, 0.1 chance that it deviates on the either side of `a`

        If I assume that the model is known, then I have access to these
        probabilities. Otherwise, I can do a lot of rollouts and estimate the
        probabilities.
        """
        a = a.upper()
        action_id = list(self.actions.keys()).index(a)
        probs = [0 for i in range(len(self.actions))]
        probs[action_id] = 0.8
        probs[(action_id + len(self.actions) + 1) % len(self.actions)] = 0.1
        probs[(action_id + len(self.actions) - 1) % len(self.actions)] = 0.1
        print("actions:", list(self.actions.keys()))
        print(probs)
        executed_action = list(self.actions.keys())[np.random.choice(4, p=probs)]


        # Check bounds
        row = s[0] + self.actions[executed_action][0]
        col = s[1] + self.actions[executed_action][1]
        print("Action: ", executed_action, self.actions[executed_action])

        if self.isValid((row, col)):
            return (row, col)
        else:
            # Stay in place
            return s

