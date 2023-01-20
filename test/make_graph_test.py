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
    g = Graph(len(graph_data))
    for i in range(len(graph_data)):
        if graph_data[i] == "1":
            right = i % n
            left = int((i - (i % n)) / n)
            g.connect_vertex(left, [right])
    return g

# %%
def create_graph_data(files, count):
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
def find_iso_class (path):
    iso_class = ["stopper"]
    for files in os.listdir(path):
     if files.endswith('.txt'):
        head, sep, tail = files.partition('.')
        iso_class.append(head + '.solution')
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
                    iso_class.append(head + '.solution')
        iso_class.append("stopper")
    return iso_class

# %%
def delete_iso (iso_class, path):
    keep_class = []
    garbage = []
    for i in range(len(iso_class) - 1):
        if (iso_class[i] == "stopper") and (iso_class[i+1] not in garbage):
            keep_class.append(iso_class[i+1])
        garbage.append(iso_class[i])
            
    for files in os.listdir(path):
     if ((files not in keep_class) and (files in iso_class)) or (files.endswith('.txt')):
        print("files to be removed " + files)
        os.remove(files)

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
            print(files)

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
        
iso_class = find_iso_class(path)
delete_iso(iso_class, path)


