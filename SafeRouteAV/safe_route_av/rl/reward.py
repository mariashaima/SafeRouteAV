def compute_reward(progress, collision, ttc, lane_dev):
    reward = 0.0

    reward += 1.0 * progress

    if collision:
        reward -= 100.0

    if ttc < 2.0:
        reward -= 10.0

    reward -= 0.1 * lane_dev

    return reward
