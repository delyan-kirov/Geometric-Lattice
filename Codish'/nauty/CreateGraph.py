#%% Imports
from math import sqrt
import re
import sys

#%% Get file
file = sys.argv[1]
index = file.split("geo-n-")[1].split(".solution")[0]
print (index)
content = ''
with open(file, 'r') as file:
    content = file.read()
# print(content)

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
print(n)

cover = list(map(lambda xs : int(xs[-1]), cover))
# print (cover)

graphMatrix = []
while cover != []:
    graphMatrix.append(cover[0:n])
    cover = cover[n:]
# print(graphMatrix)

#%% Print result

result = "G" + index + " := DigraphByAdjacencyMatrix(" + str(graphMatrix) + ");"

with open("data.g", 'a') as f:
    f.write(result + "\n")