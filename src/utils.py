from pathlib import Path
from simple_graph import SimpleGraph

def new_graph(file: Path):
  with file.open("r", encoding="utf-8") as f:
    V = int(f.readline())
    E = int(f.readline())
    g = SimpleGraph(V)
    for _ in range(E):
      v, w = f.readline().split()
      g.add_edge(v, w)
  return g