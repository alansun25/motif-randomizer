import networkx as nx
import random

# Get input graph.
def get_graph():
  try:
    # Get input graph.
    with open(input('Provide path to graph file: '), 'r') as input_graph:
      G = nx.read_weighted_edgelist(input_graph, create_using=nx.DiGraph, nodetype = int)
    input_graph.close()
    
    return G
  except FileNotFoundError:
    print("FileNotFoundError: Invalid file or directory. Check the file exists and try again.")

# Get motif of interest.
def get_motif():
  motifs = open('motifs.txt', 'r')
  motif_prompt = motifs.read()
  
  chosen_motif = input(
    motif_prompt + "\n" +
    "Choose one motif listed above (1 - 13) of which you'll change its frequency: "
  )
  while not chosen_motif.isnumeric() or int(chosen_motif) < 1 or int(chosen_motif) > 13:
    chosen_motif = input(
      motif_prompt + "\n" + "Please enter a number between 1 and 13: "
    )
  
  motifs.close()
  
  return chosen_motif

# Get frequency change (increasing or decreasing).
def get_freq_change():
  freq = input("Increase or decrease frequency of motif? (i or d): ")
  while freq != "i" and freq != "d":
    freq = input("Please enter i or d: ")
    
  return freq

# Select two random edges from a given edge list.
def random_vertices(edges):
  u = random.choice(edges)
  v = random.choice(
    # Enforce selection of two different edges without any shared nodes
    [e for e in edges if len(set([u[0], u[1], e[0], e[1]])) == 4]
  )
  
  return u, v

# Swap two edges in graph G.
#
# TODO: Bias the edge swap (decide whether to accept or discard the edge swap 
# based on something related to the specified motif). Can accept swaps that 
# increase or keep frequency same (soft bias).
def swap_edge(G, motif, freq):
  edges = list(G.edges)
  u, v = random_vertices(edges)

  # Prevent multi-edge
  while G.has_edge(u[0], v[1]) or G.has_edge(v[0], u[1]):
    u, v = random_vertices(edges)

  G.remove_edge(u[0], u[1])
  G.remove_edge(v[0], v[1])
  
  G.add_edge(u[0], v[1])
  G.add_edge(v[0], u[1])
  
  return G

# Randomize graph G using biased link randomization, maintaining degree sequence.
def randomize(G):
  motif, freq = get_motif(), get_freq_change()
  
  steps = 10 * G.number_of_edges()
  for _ in range(0, steps):
    G = swap_edge(G, motif, freq)
  
  return G

# Return the degree sequence of graph G.
def degree_sequence(G):
  return [d for _, d in G.degree()]

# TODO: Show figures of the changing of network parameters such as the
# average clustering coefficient, assortativity coefficient, average shortest
# path length, etc., during the randomization.

def main():
  G = get_graph()
  r_G = randomize(G)
  
  print(degree_sequence(G))
  print(degree_sequence(r_G))

if __name__ == '__main__':
  main()