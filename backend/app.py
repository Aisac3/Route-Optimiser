from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import osmnx as ox
import networkx as nx
import numpy as np
from tsp_nn import nearest_neighbor_tsp
from tsp_2opt import two_opt, calculate_total_distance
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load graph once at startup
G = ox.load_graphml("ernakulam_drive.graphml")

# ----- Helper Functions -----

def get_nearest_node(lat, lon):
    return ox.distance.nearest_nodes(G, lon, lat)

def road_distance(node1, node2):
    route = nx.astar_path(G, node1, node2, weight="length")
    return nx.path_weight(G, route, weight="length")

def build_distance_matrix(stops):
    nodes = [get_nearest_node(stop.lat, stop.lon) for stop in stops]
    n = len(nodes)
    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            dist = road_distance(nodes[i], nodes[j])
            matrix[i][j] = dist
            matrix[j][i] = dist

    return matrix, nodes

def reconstruct_full_route(nodes, route_order):
    full_path = []

    for i in range(len(route_order) - 1):
        origin = nodes[route_order[i]]
        destination = nodes[route_order[i + 1]]

        segment = nx.astar_path(G, origin, destination, weight="length")

        if i > 0:
            segment = segment[1:]

        full_path.extend(segment)

    return full_path

# ----- Request Model -----

class Stop(BaseModel):
    lat: float
    lon: float

class OptimizeRequest(BaseModel):
    stops: List[Stop]

# ----- API Endpoint -----

@app.post("/optimize")
def optimize_route(data: OptimizeRequest):
    stops = data.stops

    matrix, nodes = build_distance_matrix(stops)

    route, _ = nearest_neighbor_tsp(matrix)
    improved_route = two_opt(route, matrix)
    total_distance = calculate_total_distance(improved_route, matrix)

    full_nodes = reconstruct_full_route(nodes, improved_route)

    # Convert node IDs to coordinates
    route_coordinates = [
        [G.nodes[node]['y'], G.nodes[node]['x']]
        for node in full_nodes
    ]

    return {
        "optimized_order": improved_route,
        "total_distance_meters": total_distance,
        "route_coordinates": route_coordinates
    }