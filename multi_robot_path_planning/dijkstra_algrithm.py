import heapq
import sys
from multi_robot_path_planning.graph import Graph


class DijkstraPathFinding():
    def __init__(self) -> None:
        pass

    def find_shorest_path(self, start, goal, graph: Graph, crowed_edges: dict):
        print(crowed_edges)
        distances = {}  # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = []  # Priority queue of all nodes in Graph
        for vertex in graph.vertices:
            if vertex == start:  # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None

        step = 0
        while nodes:
            # Vertex in nodes with smallest distance in distances
            smallest = heapq.heappop(nodes)[1]
            step += 1
            if smallest == goal:  # If the closest node is our target we're done so print the path
                path = []
                # Traverse through nodes til we reach the root which is 0
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                path.append(start)
                return list(reversed(path))
            # All remaining vertices are inaccessible from source
            if distances[smallest] == sys.maxsize:
                break

            # Look at all the nodes that this vertex is attached to
            for neighbor in graph.vertices[smallest]:
                print(
                    f"Step: {step} - Edge {smallest}, {neighbor}")

                # Alternative path distance
                alt = distances[smallest] + \
                    graph.vertices[smallest][neighbor]
                if (step in crowed_edges) and ([smallest, neighbor] in crowed_edges[step]):
                    alt += 1000
                    print(
                        f"Edge {smallest}, {neighbor} in crowed edges at {step}")
                # If there is a new shortest path update our priority queue (relax)
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances

    def print_f(self):
        print("hello world")
