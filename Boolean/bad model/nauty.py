# %%
import re
import networkx as nx
import math
from pathlib import Path
import os
from pynauty import *

# %%
def make_graph(graph_data):
    n = int(math.sqrt(len(graph_data)))
    g = Graph(n)
    for i in range(len(graph_data)):
        if graph_data[i] == "1":
            right = i % n
            left = int((i - (i % n)) / n)
            g.connect_vertex(left, [right])
    return g

# %%
def create_graph_data(files, count):
    with open(files, "r") as file:
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
        f.close
        file.close()
    pass

# %%
def prep_cover(path):
    for files in os.listdir(path):
        if files.endswith('.solution'):
            with open(files, 'r+') as file:
                data = file.read().replace('\n', '')
                sep = 'letting J'
                data = data.split(sep, 1)[0]
                head, sep, tail = file.name.partition('.')
                newfile = open(head + ".cover", "w+")
                newfile.write(data)
                os.remove(files)
                file.close()

# %%
def rename_cover(path):
    for files in os.listdir(path):
        if files.endswith('.cover'):
            head, sep, tail = files.partition('.')
            os.rename(files, head + '.solution')

# %%
def find_file_type(path, extension):
    data = []
    for files in os.listdir(path):
        if files.endswith(extension):
            with open(files, 'r+') as file:
                data.append(files)
                file.close
    return data

# %%
def remove_iso (graph_data):
    iso_class = []
    while graph_data != []:
        rep = graph_data[0]
        iso_class.append(rep)
        with open(rep, 'r') as file:
                graph_rep = make_graph(file.read())
                file.close
        graph_data_copy = graph_data[:]
        for data in graph_data_copy:
            with open(data, 'r') as file:
                graph_i = make_graph(file.read())
                file.close
            if isomorphic(graph_i, graph_rep):
                graph_data.remove(data)
    print("Found isomorphic classes" + " , There are " + str(len(iso_class)))
    return iso_class
                

# %%
def delete_iso (iso_class, path):
    # Find .solution files corresponding with .txt files
    print("Deleting isomorphic lattices")
    solutions = []
    for data in iso_class:
        head, sep, tail = data.partition('.')
        solution = head + ".solution"
        solutions.append(solution)
    for files in os.listdir(path):
        if (files not in solutions) and files.endswith(".solution"):
            os.remove(files)
            
# %%
def automorphims(data):
    count = 1
    for graph in data:
        with open(graph, 'r') as file:
            graph_image = make_graph(file.read())
            file.close
        graph_image.set_vertex_coloring([set([0])])
        group = str(autgrp(graph_image))
        head, sep, tail = group.partition(']], ')
        group = tail
        head, sep, tail = group.partition('.')
        group = head
        print("Group" +str(count) + " size is " + group)
        count = count + 1
        


# %%
# Main
path = Path(".")  # current directory
prep_cover(path)
rename_cover(path)
extension = ".solution"
count = 0
for files in os.listdir(path):
    count = count + 1
    if files.endswith(extension):
        create_graph_data(files, count)
graph_data = find_file_type(".", ".txt")
iso_class = remove_iso(graph_data)
automorphims(iso_class)
delete_iso(iso_class, ".")


