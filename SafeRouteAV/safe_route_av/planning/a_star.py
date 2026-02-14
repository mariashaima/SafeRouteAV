import heapq
import math

def heuristic(n1, n2):
    return math.hypot(n1['x'] - n2['x'], n1['y'] - n2['y'])

class AStarPlanner:
    def __init__(self, graph):
        self.graph = graph

    def plan(self, start_id, goal_id):
        G = self.graph
        open_set = []
        heapq.heappush(open_set, (0, start_id))
        came_from = {}
        g_score = {n: float('inf') for n in G.nodes}
        g_score[start_id] = 0

        while open_set:
            _, current = heapq.heappop(open_set)
            if current == goal_id:
                return self._reconstruct_path(came_from, current)

            for neighbor in G.successors(current):
                tentative_g = g_score[current] + G.edges[current, neighbor]['cost']
                if tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(G.nodes[neighbor], G.nodes[goal_id])
                    heapq.heappush(open_set, (f_score, neighbor))
        return None

    def _reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return list(reversed(path))
