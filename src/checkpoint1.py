from pathlib import Path
from utils import new_graph, print_graph


file = Path(__file__).resolve().parent / "data" / "Email-Enron.txt"

g = new_graph(file)

print_graph(g)
