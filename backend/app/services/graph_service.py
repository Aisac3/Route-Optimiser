import os
import osmnx as ox
from app.config import DISTRICT_NAME, NETWORK_TYPE

GRAPH_FILE = "district_graph.graphml"


class GraphService:
    def __init__(self):
        if os.path.exists(GRAPH_FILE):
            print("Loading graph from local file...")
            self.graph = ox.load_graphml(GRAPH_FILE)
        else:
            print("Downloading graph for the first time...")
            self.graph = ox.graph_from_place(
                DISTRICT_NAME,
                network_type=NETWORK_TYPE
            )
            ox.save_graphml(self.graph, GRAPH_FILE)
            print("Graph saved locally!")

        print("Graph ready!")

    def get_graph(self):
        return self.graph


graph_service = GraphService()