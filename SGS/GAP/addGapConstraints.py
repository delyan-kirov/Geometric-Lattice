#%%
import ast

# %% Read data
def getContent():
    with open("new.g", 'r') as f:
         output = f.read()
         f.close()
    output = output.replace("(),", "").replace("\n", "").replace(" ", "")
    output = ast.literal_eval(output)
    output = [(x - 1, y - 1) for x, y in output]
    return(output)

result = getContent()
print(result)

# %%
def getn():
    with open("n.param", "r") as f:
        output = f.read()
        f.close
    output = output.replace("letting n be ", "")
    return (int(output))
n = getn()
print(n)

bijection = [x for x in range(0, n)]
print(bijection)

# %%
def genBijection (pair, n):
    print (pair)
    bijection = [x for x in range(0, n)]
    bijection[pair[0]], bijection[pair[1]] = bijection[pair[1]], bijection[pair[0]]
    return bijection
genBijection((2,3), 4)
# %%
def make(result, n):
    output = []

    for pair in result:
        bijection = [x for x in range(0, n)]
        bijection[pair[0]], bijection[pair[1]] = bijection[pair[1]], bijection[pair[0]]
        output.append(bijection)

    return output
make(result, n)
print(result)
# %%
# (0, 1) --> 1
# element 0 acts on element 1 and returns 1