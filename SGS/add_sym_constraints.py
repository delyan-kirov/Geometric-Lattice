# %%
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import SymmetricGroup
from array import *
import os
import re
from pathlib import Path

# %%
def extract(data):
    head, sep, tail = data.partition('), P')
    head, sep, tail = head.partition("ion")
    return tail

# %%
def clear(data, permutation):
    head, sep, tail = data.partition(permutation + "), ")
    return tail

# %%
def reshape(data, char):
   return [value for value in data if value != char]

# %%
def find_values(data):
    result = []
    refinement = []
    while data != "":
        head, sep, tail = data.partition(", ")
        result.append(head)
        data = tail

    for i in range(0, len(result)):
        if ("(" in result[i]) and (")(" not in result[i]):
            refinement.append("(")
            head, sep, tail = result[i].partition("(")
            refinement.append(tail)
        if (")" in result[i]) and (")(" not in result[i]):
            head, sep, tail = result[i].partition(")")
            refinement.append(head)
            refinement.append(")")
        if ")(" in result[i]:
            head, sep, tail = result[i].partition(")(")
            if "(" in head :
                refinement.append("(")
                head1, sep1, tail1 = head.partition("(")
                refinement.append(tail1)
            if ")" in head:
                head1, sep1, tail1 = head.partition(")")
                refinement.append(head1)
                refinement.append(")")
            
        if ("(" not in result[i]) and (")" not in result[i]):
            refinement.append(result[i])
    return refinement

# %%
def bijection(data, n):
    identity = list(range(0,n))
    for i in range(0,len(data)-1):
        if data[i] == '(':
            keep = data[i+1]
        if data[i] == ')':
            continue
        if data[i+1] == ')':
            identity[int(data[i])] = int(keep)
        if data[i+1] != ')' and (data[i] != "("):
            identity[int(data[i])] = int(data[i+1])
    return identity

# %%
def generating_set(G, n):
    data = str((G.schreier_sims_incremental(base = list(range(0,n))))[1])
    permutations = []
    i = 0
    while (data != ""):
        permutations.append(extract(data))
        data = clear(data, permutations[i])
        i = i + 1
    for i in range (0, len(permutations)-1):
        permutations[i] = permutations[i] + ")"
        
    data = []
    normal_form = []
    
    for i in range(0, len(permutations)-1):
        data = find_values(permutations[i])
        normal_form.append(bijection(data, n))
    
    return normal_form
        

# %%
def get_n():
    with open ("n.param", 'r') as f:
         data = f.read()
         n = data.split("letting n be ",1)[1]
         f.close()
    return int(n)

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
print("adding constraints")
permutations = generating_set(SymmetricGroup(n), n)
constraints = sat_model(permutations, n) + "letting sizeS be " + str(len(permutations)-1)
with open("n.param", 'a') as file:
    file.write(constraints)


