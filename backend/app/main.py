from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.services.graph_service import graph_service
from app.services.geocoder_service import geocoder_service
from app.services.path_service import path_service
from app.services.tsp_service import tsp_service


# -----------------------
# Pydantic Model
# -----------------------
class Coordinate(BaseModel):
    lat: float
    lng: float


# -----------------------
# FastAPI Setup
# -----------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------
# Startup Event
# -----------------------
@app.on_event("startup")
def startup_event():
    graph_service.get_graph()


# -----------------------
# Root
# -----------------------
@app.get("/")
def root():
    return {"message": "SmartRoute Backend Running 🚀"}


# -----------------------
# Geocoding
# -----------------------
@app.get("/geocode")
def geocode(place: str = None, lat: float = None, lng: float = None):

    if place:
        results = geocoder_service.geocode_location(place)
        if not results:
            return {"error": "Location not found"}
        return results

    if lat and lng:
        result = geocoder_service.reverse_geocode(lat, lng)
        if not result:
            return {"error": "Location not found"}
        return result

    return {"error": "Invalid parameters"}


# -----------------------
# Optimize using names
# -----------------------
@app.post("/optimize-route")
def optimize_route(stops: list[str]):

    if len(stops) < 2:
        return {"error": "At least 2 stops required"}

    nodes = []

    for stop in stops:
        results = geocoder_service.geocode_location(stop)

        if not results or not isinstance(results, list):
            return {"error": f"Location not found: {stop}"}

        coords = results[0]

        node = path_service.get_nearest_node(
            coords["lat"],
            coords["lng"]
        )

        nodes.append(node)

    return process_optimization(nodes)


# -----------------------
# Optimize using coordinates
# -----------------------
@app.post("/optimize-coordinates")
def optimize_coordinates(coords: list[Coordinate]):

    if len(coords) < 2:
        return {"error": "At least 2 points required"}

    nodes = []

    for c in coords:
        node = path_service.get_nearest_node(c.lat, c.lng)
        nodes.append(node)

    return process_optimization(nodes)


# -----------------------
# Shared Optimization Logic
# -----------------------
def process_optimization(nodes):

    matrix, path_cache = tsp_service.build_distance_matrix(nodes, path_service)

    initial_order = tsp_service.nearest_neighbor(matrix)
    order = tsp_service.two_opt(initial_order, matrix)

    full_route = []
    total_distance = 0
    segment_distances = []

    for i in range(len(order) - 1):

        segment = path_cache[(order[i], order[i + 1])]

        if i > 0:
            segment = segment[1:]  # remove duplicate node

        full_route.extend(segment)

        segment_length = matrix[order[i]][order[i + 1]]
        total_distance += segment_length

        # Convert meters to KM
        segment_distances.append(round(segment_length / 1000, 2))

    route_coords = path_service.get_route_coordinates(full_route)

    return {
        "optimized_order": order,
        "total_distance_km": round(total_distance / 1000, 2),
        "segment_distances": segment_distances,
        "route": route_coords
    }