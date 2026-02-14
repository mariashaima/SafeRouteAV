import ray
from ray.rllib.algorithms.ppo import PPOConfig
from safe_route_av.carla_interface.carla_env import CarlaRouteEnv


def train():

    ray.init(ignore_reinit_error=True)

    config = (
        PPOConfig()
        .environment(CarlaRouteEnv)
        .framework("torch")
        .rollouts(num_rollout_workers=1)
    )

    algo = config.build()

    for i in range(100):
        result = algo.train()
        print(f"Iteration {i}: reward {result['episode_reward_mean']}")

    algo.save("experiments/models/")
