from pathlib import Path
from algs4 import graph

def new_graph(file: Path) -> graph.Graph:
  with file.open("r", encoding="utf-8") as f:
    V = int(f.readline())
    E = int(f.readline())
    g = graph.Graph(V)
    for _ in range(E):
      v, w = f.readline().split()
      add_one_edge(g, v, w)
      # g.add_edge(v, w)
  return g

def add_one_edge(g: graph.Graph, v: int, w: int) -> None:
  v, w = int(v), int(w)
  g.adj[v].add(w)
  # g.adj[w].add(v)
  g.E += 1

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
