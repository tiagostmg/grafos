from pathlib import Path
from algs4 import graph

def new_graph(file: Path) -> graph.Graph:
  with file.open("r", encoding="utf-8") as f:
    V = int(f.readline())
    E = int(f.readline())
    g = graph.Graph(V)
    for _ in range(E):
      v, w = f.readline().split()
      g.add_edge(v, w)
  return g

def print_graph(g: graph.Graph) -> None:
  print(f"{g.V} vertices, {g.E} edges")
  for v in range(g.V):
    neighbors = []
    node = g.adj[v].first
    while node is not None:
      neighbors.append(str(node.item))
      node = node.next
    print(f"{v}: {' '.join(neighbors)}")
