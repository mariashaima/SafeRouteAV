from src.carla_interface.carla_client import CarlaClient
from src.carla_interface.ego_vehicle import EgoVehicle
from src.planning.graph_builder import GraphBuilder
from src.planning.a_star import AStarPlanner
from src.planning.safety_layer import SafetyLayer

def main():
    client = CarlaClient(town="Town01")
    world = client.world
    carla_map = world.get_map()
    waypoints = carla_map.generate_waypoints(2.0)

    graph_builder = GraphBuilder(waypoints)
    raw_graph = graph_builder.build_graph()

    safety_layer = SafetyLayer(safety_config={"min_clearance": 1.0})
    safe_graph = safety_layer.filter_graph(raw_graph)

    start_id = waypoints[0].id
    goal_id = waypoints[100].id  # example
    planner = AStarPlanner(safe_graph)
    path_ids = planner.plan(start_id, goal_id)

    ego = EgoVehicle(world)
    path_wps = [wp for wp in waypoints if wp.id in path_ids]
    ego.follow_route(path_wps)

if __name__ == "__main__":
    main()
