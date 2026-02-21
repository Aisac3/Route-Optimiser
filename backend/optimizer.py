import osmnx as ox
import networkx as nx
import numpy as np
from tsp_nn import nearest_neighbor_tsp
from tsp_2opt import two_opt, calculate_total_distance

# Load graph once
G = ox.load_graphml("ernakulam_drive.graphml")

def get_nearest_node(lat, lon):
    return ox.distance.nearest_nodes(G, lon, lat)

def road_distance(node1, node2):
    route = nx.astar_path(G, node1, node2, weight="length")
    return nx.path_weight(G, route, weight="length")

def build_distance_matrix(stops):
    nodes = [get_nearest_node(lat, lon) for lat, lon in stops]
    n = len(nodes)
    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            dist = road_distance(nodes[i], nodes[j])
            matrix[i][j] = dist
            matrix[j][i] = dist

    return matrix

def optimize_route(stops):
    matrix = build_distance_matrix(stops)

    route, _ = nearest_neighbor_tsp(matrix)
    improved_route = two_opt(route, matrix)
    final_distance = calculate_total_distance(improved_route, matrix)

    return improved_route, final_distance

def reconstruct_full_route(stops, route_order):
    nodes = [get_nearest_node(lat, lon) for lat, lon in stops]
    full_path = []

    for i in range(len(route_order) - 1):
        origin = nodes[route_order[i]]
        destination = nodes[route_order[i + 1]]

        segment = nx.astar_path(G, origin, destination, weight="length")

        if i > 0:
            segment = segment[1:]  # avoid duplicate nodes

        full_path.extend(segment)

    return full_path

if __name__ == "__main__":
    stops = [
        (10.0159, 76.3419),
        (9.9816, 76.2999),
        (10.0300, 76.3000),
        (9.9900, 76.3500),
        (10.0500, 76.3200),
        (10.0100, 76.3300),
        (9.9700, 76.3100),
        (10.0400, 76.2900),
    ]

    route, distance = optimize_route(stops)
    full_path = reconstruct_full_route(stops, route)

    print("Optimized Visiting Order:", route)
    print("Total Road Distance (meters):", distance)
    print("Full route node count:", len(full_path))