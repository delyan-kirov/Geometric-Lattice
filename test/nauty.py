# %%
import re
import networkx as nx
import math
from pathlib import Path
import matplotlib.pyplot as plt
import os
from pynauty import *

# %%
def make_graph(graph_data):
    n = int(math.sqrt(len(graph_data)))
    g = Graph(len(graph_data))
    for i in range(len(graph_data)):
        if graph_data[i] == "1":
            right = i % n
            left = int((i - (i % n)) / n)
            g.connect_vertex(left, [right])
    return g

# %%
def graphic(files, count):
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
        head, sep, tail = file.name.partition('.')
        with open (head + '.txt', 'w') as f:
            f.write(graph_data)
            print(head)
        f.close
        file.close()
    pass

# %%
path = Path(".")  # current directory
extension = ".solution"
count = 0
delete = ["stopper"]
for files in os.listdir(path):
    count = count + 1
    if files.endswith(extension):
        graphic(files, count)
for files in os.listdir(path):
    if files.endswith('.txt'):
        head, sep, tail = files.partition('.')
        delete.append(head + '.solution')
        for files_copy in os.listdir(path):
            if files_copy.endswith('.txt'):
                with open (files_copy) as file_1:
                    graph_data_1 = file_1.read()
                file_1.close
                
                with open (files) as file_2:
                    graph_data_2 = file_2.read()
                file_2.close
                
                if (files != files_copy) and (isomorphic(make_graph(graph_data_1), make_graph(graph_data_2))):
                    head, sep, tail = files_copy.partition('.')
                    delete.append(head + '.solution')
        delete.append("stopper")
boolean_mask = []
garbage = []
for i in range(len(delete) - 1):
    if (delete[i] == "stopper") and (delete[i+1] not in garbage):
        boolean_mask.append(delete[i+1])
    garbage.append(delete[i])
for files in os.listdir(path):
    if ((files not in boolean_mask) and (files in delete)) or (files.endswith('.txt')):
        print("files to be removes" + files)
        os.remove(files)


