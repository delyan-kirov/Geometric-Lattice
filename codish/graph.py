# %%
import re
import networkx as nx
import math
from pathlib import Path
import matplotlib.pyplot as plt
import os

# %%
# initialising the graph
def make_graph(graph_data):
    graph = nx.DiGraph()
    n = int(math.sqrt(len(graph_data)))
    graph.add_nodes_from(range(0, n - 1))
    graph_edges = []
    for i in range(len(graph_data)):
        if graph_data[i] == "1":
            right = i % n
            left = int((i - (i % n)) / n)
            graph_edges.append((left, right))
    graph.add_edges_from(graph_edges)
    print("Drawing graph from solver")
    print(graph_edges)
    return graph


# %%
def draw(files, count):
    with open(files, "r") as file:
        print("opening solution from solver")
        cover = file.read()
        graph_data = ""

        # finding pattern
        pattern = re.compile(r"--> (\d+)")
        for match in pattern.finditer(cover):
            number = match.group(1)
            graph_data = "".join((graph_data, number))

        graph = make_graph(graph_data)
        nx.draw(graph, pos=nx.circular_layout(graph), with_labels=True)
        name = "graph_" + str(count) + ".png"
        print(name)
        plt.savefig(name, dpi=300, bbox_inches="tight")
        plt.close("all")
        file.close()
    pass


# %%
# drawing script
path = Path(".")  # current directory
extension = ".solution"
count = 0
for files in os.listdir(path):
    count = count + 1
    if files.endswith(extension):
        draw(files, count)
