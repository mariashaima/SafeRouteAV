import gymnasium as gym
import numpy as np
import carla
from safe_route_av.safety.carla_ttc import CarlaTTC


class CarlaRouteEnv(gym.Env):

    def __init__(self, config):
        super().__init__()

        self.client = carla.Client("localhost", 2000)
        self.client.set_timeout(10.0)
        self.world = self.client.get_world()

        self.vehicle = None
        self.route = config["route"]

        self.observation_space = gym.spaces.Box(
            low=-100, high=100, shape=(6,), dtype=np.float32
        )

        self.action_space = gym.spaces.Box(
            low=np.array([-1.0, 0.0]),
            high=np.array([1.0, 1.0]),
            dtype=np.float32
        )

    def reset(self, seed=None, options=None):
        self._spawn_vehicle()
        obs = self._get_obs()
        return obs, {}

    def step(self, action):

        steer, throttle = action

        control = carla.VehicleControl()
        control.steer = float(steer)
        control.throttle = float(throttle)

        self.vehicle.apply_control(control)

        self.world.tick()

        obs = self._get_obs()
        reward = self._compute_reward()
        done = self._check_done()

        return obs, reward, done, False, {}

    def _spawn_vehicle(self):
        blueprint = self.world.get_blueprint_library().filter("vehicle.*")[0]
        spawn_point = self.world.get_map().get_spawn_points()[0]
        self.vehicle = self.world.spawn_actor(blueprint, spawn_point)

    def _get_obs(self):
        velocity = self.vehicle.get_velocity()
        location = self.vehicle.get_location()

        return np.array([
            location.x,
            location.y,
            velocity.x,
            velocity.y,
            0.0,
            0.0
        ], dtype=np.float32)

    def _compute_reward(self):
        ttc_calc = CarlaTTC(self.vehicle, self.world)
        ttc = ttc_calc.compute_min_ttc()

        reward = 1.0
        if ttc < 2.0:
            reward -= 10.0

        return reward

    def _check_done(self):
        return False
