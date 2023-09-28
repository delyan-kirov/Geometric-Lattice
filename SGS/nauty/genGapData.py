#%% Imports
from math import sqrt
import re
import sys

#%% Get file
file = sys.argv[1]
index = file.split("geo-n-")[1].split(".solution")[0]
content = ''
with open(file, 'r') as file:
    content = file.read()

#%% Get string
content = content[len('function'):-len('letting J be')]
match = re.search(r'function([\s\S]*?)\nletting J be', content)
cover = ''

if match:
    cover = match.group(1).strip()[1:-1]
else:
    print("Substring not found.")
    
cover = cover.replace('\n', '').replace(' ', '')
cover = cover.split(',(')

n = int(sqrt(len(cover)))

cover = list(map(lambda xs : int(xs[-1]), cover))

graphMatrix = []
while cover != []:
    graphMatrix.append(cover[0:n])
    cover = cover[n:]

def adjacency_matrix_to_edges(adj_matrix):
    edges = []
    num_nodes = len(adj_matrix)

    for i in range(0,num_nodes):
        for j in range(0,num_nodes):
            if adj_matrix[i][j] == 1: edges.append([i,j])

    return edges

result = adjacency_matrix_to_edges(graphMatrix)

#%% Print result

result = "G" + index + " := " + 'GraphByEdges(' + str(result) + ");"
with open("data.g", 'a') as f:
    f.write(result + "\n")