import carla

class CarlaClient:
    def __init__(self, host="localhost", port=2000, town="Town01"):
        self.client = carla.Client(host, port)
        self.client.set_timeout(10.0)
        self.world = self.client.load_world(town)
        self.map = self.world.get_map()
