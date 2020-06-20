import numpy as np
from config import ACTIONS, ACTION_MAP, ROWS, COLS, TERMINAL


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
    # Extra element for stay-in-place action
    probs = [0 for i in range(len(ACTIONS) + 1)]
    probs[action_id] = 0.8
    probs[(action_id + len(ACTIONS) + 1) % len(ACTIONS)] = 0.1
    probs[(action_id + len(ACTIONS) - 1) % len(ACTIONS)] = 0.1
    executed_action = ACTIONS[np.random.choice(5, p=probs)]

    # Check bounds
    row = s[0] + ACTION_MAP[executed_action][0]
    col = s[1] + ACTION_MAP[executed_action][1]
    if row >= 0 and row < ROWS and col >= 0 and col < COLS:
        return (row, col)
    else:
        return s

def step(s, a):
    if s in TERMINAL:
        return (s, getReward(s))
    else:
        succ = getSuccs(s, a)
        return (succ, getReward(succ))

