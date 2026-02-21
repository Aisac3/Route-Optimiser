import osmnx as ox
import networkx as nx

# Load saved graph
G = ox.load_graphml("ernakulam_drive.graphml")

print("Graph loaded.")

def get_nearest_node(lat, lon):
    return ox.distance.nearest_nodes(G, lon, lat)


def shortest_path_distance(lat1, lon1, lat2, lon2):
    # Snap to nearest nodes
    origin = get_nearest_node(lat1, lon1)
    destination = get_nearest_node(lat2, lon2)

    # Run A* algorithm
    route = nx.astar_path(
        G,
        origin,
        destination,
        weight="length"
    )

    # Calculate total road distance
    distance = nx.path_weight(G, route, weight="length")

    return route, distance

if __name__ == "__main__":
    # Example coordinates in Ernakulam
    lat1, lon1 = 10.0159, 76.3419   # Point A
    lat2, lon2 = 9.9816, 76.2999    # Point B

    route, dist = shortest_path_distance(lat1, lon1, lat2, lon2)

    print("Road Distance (meters):", dist)
    print("Number of nodes in route:", len(route))