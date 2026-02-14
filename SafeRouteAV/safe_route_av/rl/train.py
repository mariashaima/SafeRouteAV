import ray
from ray.rllib.algorithms.ppo import PPOConfig
from safe_route_av.carla_interface.carla_env import CarlaRouteEnv


def train():

    ray.init()

    config = (
        PPOConfig()
        .environment(CarlaRouteEnv, env_config={"route": []})
        .framework("torch")
        .rollouts(num_rollout_workers=1)
        .training(model={"fcnet_hiddens": [256, 256]})
    )

    algo = config.build()

    for i in range(200):
        result = algo.train()
        print(f"Iter {i}: reward={result['episode_reward_mean']}")

    algo.save("experiments/models")
