import json
from multi_robot_path_planning.graph import Graph
from multi_robot_path_planning.dijkstra_algrithm import DijkstraPathFinding

import os

import os

absolute_path = os.path.dirname(__file__)

if __name__ == "__main__":
    f = open(os.path.join(absolute_path, "data.json"))
    data = json.load(f)

    graph = Graph()
    graph.load(data)

    dijkstra_path_finding = DijkstraPathFinding()
    path = dijkstra_path_finding.find_shorest_path("A", "H", graph)
    print(path)
