from pathlib import Path
from algs4 import graph
from algs4.utils.linklist import LinkIterator


file = Path(__file__).resolve().parent / "data" / "Email-Enron.txt"

# if not hasattr(LinkIterator, "__iter__"):
#     LinkIterator.__iter__ = lambda self: self

with file.open("r", encoding="utf-8") as f:
  print(f.readline())
#   V = int(f.readline().strip())
#   E = int(f.readline().strip())
#   g = graph.Graph(V)
#   for _ in range(V):
#       v, w = f.readline().strip().split()
#       g.add_edge(v, w)
# print(g)
