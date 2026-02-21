import osmnx as ox
import networkx as nx
from app.services.graph_service import graph_service


class PathService:
    def __init__(self):
        self.graph = graph_service.get_graph()

    def get_nearest_node(self, lat: float, lng: float):
        return ox.distance.nearest_nodes(self.graph, lng, lat)

    def shortest_path(self, start_node, end_node):
        try:
            route = nx.shortest_path(
                self.graph,
                start_node,
                end_node,
                weight="length"
            )
            return route
        except nx.NetworkXNoPath:
            return None

    def calculate_route_length(self, route):
        total_length = 0
        for i in range(len(route) - 1):
            edge_data = self.graph.get_edge_data(route[i], route[i+1])
            if edge_data:
                edge = list(edge_data.values())[0]
                total_length += edge.get("length", 0)
        return total_length

    def get_route_coordinates(self, route):
        coords = []
        for node in route:
            point = self.graph.nodes[node]
            coords.append({
                "lat": point["y"],
                "lng": point["x"]
            })
        return coords
    def build_full_route(self, ordered_nodes):
        full_route = []
        total_distance = 0

        for i in range(len(ordered_nodes) - 1):
            segment = self.shortest_path(
                ordered_nodes[i],
                ordered_nodes[i+1]
            )

            if not segment:
                continue

            if i > 0:
                segment = segment[1:]  # avoid duplicate node

            full_route.extend(segment)
            total_distance += self.calculate_route_length(segment)

        route_coords = self.get_route_coordinates(full_route)
        return route_coords, total_distance
    


path_service = PathService()