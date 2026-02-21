import osmnx as ox
import networkx as nx
import numpy as np

G = ox.load_graphml("ernakulam_drive.graphml")

def get_nearest_node(lat, lon):
    return ox.distance.nearest_nodes(G, lon, lat)

def road_distance(node1, node2):
    route = nx.astar_path(G, node1, node2, weight="length")
    return nx.path_weight(G, route, weight="length")

stops = [
    (10.0159, 76.3419),
    (9.9816, 76.2999),
    (10.0300, 76.3000),
    (9.9900, 76.3500),
    (10.0500, 76.3200),
]

nodes = [get_nearest_node(lat, lon) for lat, lon in stops]

n = len(nodes)
matrix = np.zeros((n, n))

for i in range(n):
    for j in range(i + 1, n):
        dist = road_distance(nodes[i], nodes[j])
        matrix[i][j] = dist
        matrix[j][i] = dist

print(matrix)