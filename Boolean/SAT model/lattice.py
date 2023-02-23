# %%
def make_graph(n):
    n = 2**n
    graph = [[]]
    for i in range(0,n):
        graph.append([0])
        for j in range(0,n-1):
            graph[i].append(0)
    
    graph[0].append(0)
    graph.pop()
    return(graph)

# %%
def make_subsets(n):
    set = list(range(1,n+1))
    subsets = [[]]
    for el in set:
        for i in range(len(subsets)):
            subsets += [subsets[i]+[el]]
    subsets.sort(key=len)
    return(subsets)

# %%
def make_lattice(n):
    size = 2**n
    subsets = make_subsets(n)
    graph = make_graph(n)
    for j in subsets:
        for i in subsets:
           check =  all(item in i for item in j)
           if check == True and (len(i) - len(j) == 1):
                graph[subsets.index(j)][subsets.index(i)] = 1
                graph[subsets.index(i)][subsets.index(j)] = 1
    return(graph)


# %%
def sat_model(lattice, n):
    string = "letting lattice be function("
    value = ""
    for i in range(0, 2**n):
        for j in range (0, 2**n):
            value = "(" + str(i) + ", " + str(j) + ")" + " --> " + str(lattice[i][j]) + ", " + "\n"
            string = string + value
            value = ""
    string = string + ") " + "\n letting n be " + str(2**n)
    return string

# %%
#main
n = input("size of lattice ")
n = int(n)
lattice = make_lattice(n)
model = sat_model(lattice,n)
with open("n.param", 'a') as file:
      file.write(model)


