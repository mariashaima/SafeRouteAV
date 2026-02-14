import numpy as np

class RouteFollowerAgent:
    def __init__(self, policy):
        self.policy = policy  # e.g., a PyTorch model

    def act(self, observation, target_waypoint):
        # observation: sensors, ego state
        # target_waypoint: next point on A* path
        input_vec = np.concatenate([observation, target_waypoint])
        action = self.policy(input_vec)
        return action
