import osmnx as ox

place_name = "Ernakulam, Kerala, India"

# Download graph (already simplified by default)
G = ox.graph_from_place(place_name, network_type='drive')

print("Nodes:", len(G.nodes))
print("Edges:", len(G.edges))

# Save graph
ox.save_graphml(G, "ernakulam_drive.graphml")

print("Graph saved successfully.")