import matplotlib.pyplot as plt
import networkx as nx

# Create a graph
G = nx.DiGraph()

# Add nodes
ksa_strategies = ['Vision 2030', 'National Innovation Plan', 'National Water Strategy 2030', "Saudi Arabia's Drought Management Strategy"]
international_agreements = ['Paris Agreement', 'UN Convention for Combatting Desertification', 'SDG 6', 'SDG 9', 'SDG 13', 'GPAI']

# Add nodes to the graph
G.add_nodes_from(ksa_strategies)
G.add_nodes_from(international_agreements)

# Define connections with their respective colors
edges = [
    ('Vision 2030', 'Paris Agreement', 'red'),
    ('Vision 2030', 'UN Convention for Combatting Desertification', 'red'),
    ('Vision 2030', 'SDG 13', 'red'),
    ('Vision 2030', 'SDG 6', 'red'),
    ('Vision 2030', 'SDG 9', 'red'),
    ('Vision 2030', 'GPAI', 'red'),
    
    ('National Innovation Plan', 'UN Convention for Combatting Desertification', 'green'),
    ('National Innovation Plan', 'SDG 13', 'green'),
    ('National Innovation Plan', 'SDG 9', 'green'),
    ('National Innovation Plan', 'GPAI', 'green'),
    
    ('National Water Strategy 2030', 'UN Convention for Combatting Desertification', 'purple'),
    ('National Water Strategy 2030', 'SDG 6', 'purple'),
    
    ("Saudi Arabia's Drought Management Strategy", 'Paris Agreement', 'blue'),
    ("Saudi Arabia's Drought Management Strategy", 'UN Convention for Combatting Desertification', 'blue'),
    ("Saudi Arabia's Drought Management Strategy", 'SDG 13', 'blue'),
    ("Saudi Arabia's Drought Management Strategy", 'SDG 6', 'blue'),
    ("Saudi Arabia's Drought Management Strategy", 'SDG 9', 'blue'),
    ("Saudi Arabia's Drought Management Strategy", 'GPAI', 'blue')
]

# Add edges to the graph with color attribute
for edge in edges:
    G.add_edge(edge[0], edge[1], color=edge[2])

# Define layout
pos = {
    'Vision 2030': (1, 3),
    'National Innovation Plan': (1, 2),
    'National Water Strategy 2030': (1, 1),
    "Saudi Arabia's Drought Management Strategy": (1, 0),

    'Paris Agreement': (3, 3),
    'UN Convention for Combatting Desertification': (3, 2),
    'SDG 6': (3, 1),
    'SDG 9': (3, 0),
    'SDG 13': (3, -1),
    'GPAI': (3, -2)
}

# Draw the graph
plt.figure(figsize=(12, 8))

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightblue', edgecolors='black')

# Draw edges with specified colors and thickness
edges_colors = [G[u][v]['color'] for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='->', arrowsize=20, edge_color=edges_colors, width=3)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

plt.title('KSA Strategies and International Agreements/SDGs Connections')
plt.axis('off')
plt.show()
