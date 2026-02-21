import osmnx as ox

place_name = "Ernakulam, Kerala, India"
G = ox.graph_from_place(place_name, network_type='drive')

print("Nodes:", len(G.nodes))
print("Edges:", len(G.edges))