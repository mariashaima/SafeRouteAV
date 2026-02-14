from safe_route_av.planning.astar import AStarPlanner
from safe_route_av.planning.heuristic import euclidean

graph = {
    (0, 0): [((1, 0), 1), ((0, 1), 1)],
    (1, 0): [((1, 1), 1)],
    (0, 1): [((1, 1), 1)],
    (1, 1): []
}

planner = AStarPlanner(graph, euclidean)

path = planner.search((0, 0), (1, 1))
print("Path:", path)
