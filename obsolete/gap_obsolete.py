# %%
from array import *
import os
import re
from pathlib import Path


# %%
def clear (data):
    permutations = []
    while data != "":
        head, sep, tail = data.partition("(")
        perm_i = tail
        head, sep, tail = perm_i.partition(")")
        perm_i = head
        permutations.append(str(perm_i))
        head, sep, tail = data.partition("), ")
        data = tail
    return permutations

# %%
def make (permutations, n):
    bijections = []
    identity = list(range(1, n+1))
    for i in range(0, len(permutations)):
        proj_l, sep, proj_r = permutations[i].partition(",")
        bijection = list(range(1, n+1))
        for j in range (1, n):
            if identity[j] == int(proj_r):
                bijection[j] = int(proj_l)
            if identity[j] == int(proj_l):
                bijection[j] = int(proj_r)
        bijections.append(bijection)

    for i in range(0, len(permutations)):
            bijections[i] = [x - 1 for x in bijections[i]]
    return(bijections)

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

# %%
#Main
path = Path(".")
n = get_n()
data = get_gap_file()
permutations = clear(data)
bijections = make(permutations, n)
constraints = sat_model(bijections, n) + "letting sizeS be " + str(len(permutations)-1)
with open("n.param", 'a') as file:
    file.write(constraints)
