# %%
from array import *
import os
import re
from pathlib import Path



# %%
def get_n():
    with open ("n.param", 'r') as f:
         data = f.read()
         n = data.split("letting n be ",1)[1]
         f.close()
    return int(n)

# %%
def get_gap_file():
    with open ("new.g", 'r') as f:
         data = f.read()
         f.close()
    return data

# %%
def refine(permutation):
    subcycles = []

    while permutation != "":
        head,sep,tail = permutation.partition(")")
        subcycles.append(head + ")")
        permutation = tail

    return(subcycles)

#%%
def clear (cycle):
    result = []
    head,sep,tail = cycle.partition("(")
    head,sep,tail = tail.partition(")")
    cycle = head
    
    while cycle != "":
        head,sep,tail = cycle.partition(",")
        result.append(int(head))
        cycle = tail
    return result

#%%
def bij(cycle, n, bijection):
    identity = list(range(1,n+1))
    
    for i in range(0,len(identity)):
        for j in range(0, len(cycle)):
            if identity[i] == cycle[j]:
                if j == len(cycle) - 1:
                    bijection[i] = cycle[0]
                    break
                bijection[i] = cycle[j+1]
                break
    return(bijection)

#%%
def extract(data):
    head, sep, tail = data.partition("[ ")
    data = tail
    head,sep,tail = data.partition(" ]")
    data = head

    data = data.replace(" ", "")
    data = data.replace("\n", "")
    data = data + ","
   
    cycles = []

    while data != "":
        head, sep, tail = data.partition("(")
        head, sep, tail = tail.partition("),")
        cycles.append("(" + head + ")")
        data = tail
    return(cycles)

#%%
def sat_model(permutations, n):
    string = "letting SGS be function("
    value = ""
    for p in range(0, len(permutations)):
        for i in range (0, n):
            value = "(" + str(p) + ", " + str(i) + ")" + " --> " + str(permutations[p][i]) + ", " + "\n"
            string = string + value
            value = ""
    string = string + ") " + "\n"
    return string

#%%
def make():
    n = get_n()
    data = get_gap_file()
    bijections = []
    data = extract(data)
    
    for i in range(0, len(data)):
        bijections.append(refine(data[i]))
    
    for i in range(0, len(bijections)):
        for j in range(0, len(bijections[i])):
            bijections[i][j] = clear(bijections[i][j])

    identity = list(range(1,n+1))
    permutations = []

    for i in range(0, len(bijections)):
        for j in range(0, len(bijections[i])):
            if j == 0:
                bijection = bij(bijections[i][j], n, identity)
            bijection = bij(bijections[i][j], n, bijection)
        permutations.append(bijection[:])
  
    for i in range(0,len(permutations)):
        for j in range(0,len(permutations[i])):
            permutations[i][j] = permutations[i][j] - 1
    
    #print(permutations)
    constraints = sat_model(permutations, n) + "letting sizeS be " + str(len(permutations)-1)
    with open("n.param", 'a') as file:
      file.write(constraints)


# %%
#Main
print("generating constaints")
make()
