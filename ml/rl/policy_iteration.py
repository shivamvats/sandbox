import numpy as np

ACTIONS = ['L', 'R', 'U', 'D']
# In terms of (row, col)
ACTION_MAP = {
        'L' : (0, -1)
        'R' : (0, +1)
        'U' : (+1, 0)
        'D' : (-1, 0)
        }
ENV = getEnv()
ROWS = 3
COLS = 4

def getEnv():
    env = np.zeros((3, 4))
    env[1, 1] = 1
    return env

def getReward(s):
    if s == (0, 3):
        return 1
    elif s == (1, 3):
        return -1
    else:
        return 0

def getSuccs(s, actuated_action):
    """Model vs model-free

    Underlying transition model: 0.8 chance that agents goes in the `a`
    direction, 0.1 chance that it deviates on the either side of `a`

    If I assume that the model is known, then I have access to these
    probabilities. Otherwise, I can do a lot of rollouts and estimate the
    probabilities.
    """
    a = actuated_action.upper()
    action_id = ACTIONS.index(a)
    probs = [0 for action in actions]
    probs[action_id] = 0.8
    probs[(action_id + len(actions) + 1) % len(actions)] = 0.1
    probs[(action_id + len(actions) - 1) % len(actions)] = 0.1
    executed_action = np.random.choice(4, p=probs)

    row = (s[0] + ACTION_MAP[executed_action][0] + ROWS) % ROWS
    col = (s[1] + ACTION_MAP[executed_action]1] + COLS) % COLS
    return (row, col)

def step(s, a):
    succ = getSuccs(s, a)
    return (succ, getReward(succ))

if __name__ == "__main__":
    """This script explores Policy Iteration for a 4x3 grid with one obstacle
    The grid looks like this

    o o o  1
    o x o -1 
    0 0 0  0

    The example is motivated by Andrew Ng's lecture on the same:
        https://www.youtube.com/watch?v=d5gaWTo6kDM 

    Policy Iteration
    """

