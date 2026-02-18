from pathlib import Path
from utils import new_graph, print_graph


file = Path(__file__).resolve().parent / "data" / "Email-Enron.txt"

g = new_graph(file)

# print_graph(g)


import matplotlib.pyplot as plt

qty_edges = lambda x : int(x.size() / 2)

data = [qty_edges(g.adj[i]) for i in range(g.V)]

plt.hist(data, bins=30, color='skyblue', edgecolor='black')

plt.show()