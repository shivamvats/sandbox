import numpy as np
from config import ACTIONS, ACTION_MAP, ROWS, COLS, GAMMA
from env import getEnv, step

ENV = getEnv()
V = np.full_like(ENV, -float('inf'))

def printEnv():
    print(ENV)

def printV():
    print(V)

if __name__ == "__main__":
    """This script explores Value Iteration for a 3x4 grid with one obstacle
    The grid looks like this

    o o o  1
    o x o -1 
    0 0 0  0

    The example is motivated by Andrew Ng's lecture on the same:
        https://www.youtube.com/watch?v=d5gaWTo6kDM 

    Value Iteration
    """
    epochs = 10
    for i in range(epochs):
        for r in range(ROWS):
            for c in range(COLS):
                q_s_a = [0.0 for a in ACTIONS]
                for action in ACTIONS:
                    succ, reward = step((r, c), action)
                    q_s_a.append(reward + GAMMA * V[succ])
                    print("Reward: %d" % reward)
                old_v = V[r, c]
                V[r, c] = max(q_s_a)
                print("V: Before: %f, After: %f" % (old_v, V[r, c]))
        printEnv()
        printV()

