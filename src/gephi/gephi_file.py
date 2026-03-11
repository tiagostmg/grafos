from pathlib import Path
import pandas as pd

file = Path(__file__).resolve().parent / "data" / "Email-Enron.txt"

def generate_csv(file: Path):
  edges = []
  with file.open("r", encoding="utf-8") as f:
    _ = f.readline()
    E = int(f.readline())
    for _ in range(E*2):
      v, w = f.readline().split()
      v, w = int(v), int(w)
      edges.append((v, w))
  return pd.DataFrame(edges, columns=["source", "target"])

def generate_csv_2(file: Path):
  edges = []
  with file.open("r", encoding="utf-8") as f:
    _ = f.readline()
    E = int(f.readline())
    for _ in range(E*2):
      edge = f.readline().strip()
      edges.append(" ".join(edge.split()))
  return pd.DataFrame(edges, columns=["edges"])

if __name__ == "__main__":
  df = generate_csv(file)
  df.to_csv(file.with_name("source-target.csv"), index=False)
  print(df.head())

  df2 = generate_csv_2(file)
  df2.to_csv(file.with_name("edges.csv"), index=False)
  print(df2.head())

# Colocamos o csv no gephi.