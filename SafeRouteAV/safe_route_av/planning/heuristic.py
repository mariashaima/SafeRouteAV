import numpy as np


def euclidean(node, goal):
    return np.linalg.norm(np.array(node) - np.array(goal))


def manhattan(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
