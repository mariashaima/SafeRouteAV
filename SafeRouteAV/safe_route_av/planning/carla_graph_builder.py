import networkx as nx
import numpy as np

class GraphBuilder:
    def __init__(self, waypoints, speed_limits=None):
        self.waypoints = waypoints
        self.speed_limits = speed_limits

    def build_graph(self) -> nx.DiGraph:
        G = nx.DiGraph()
        for wp in self.waypoints:
            G.add_node(wp.id, x=wp.transform.location.x, y=wp.transform.location.y)

        for wp in self.waypoints:
            for nxt in wp.next(2.0):  # 2m ahead
                cost = np.linalg.norm(
                    np.array([wp.transform.location.x, wp.transform.location.y]) -
                    np.array([nxt.transform.location.x, nxt.transform.location.y])
                )
                G.add_edge(wp.id, nxt.id, cost=cost)
        return G
