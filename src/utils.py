from pathlib import Path
from algs4 import graph

def new_graph(file: Path) -> graph.Graph:
  with file.open("r", encoding="utf-8") as f:
    V = int(f.readline())
    E = int(f.readline())
    g = graph.Graph(V)
    for _ in range(E):
      v, w = f.readline().split()
      # node = g.adj[int(v)].first
      # while node is not None:
      #   if node.item == int(w):
      #     continue
      #   node = node.next
      g.add_edge(v, w)
  return g

def print_graph(g: graph.Graph) -> None:
  print(f"{g.V} vertices, {g.E} edges")
  for v in range(g.V):
    neighbors = set()
    print(f"{v}: ", end="")
    node = g.adj[v].first
    while node is not None:
      print(f"{str(node.item)} ", end="")
      node = node.next
    print()
