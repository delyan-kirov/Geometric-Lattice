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

def getn():
    with open("n.param", "r") as f:
        output = f.read()
        f.close
    output = output.replace("letting n be ", "")
    return (int(output))

# %%
def genBijections(result, n):
    output = []

    for pair in result:
        bijection = [x for x in range(0, n)]
        bijection[pair[0]], bijection[pair[1]] = bijection[pair[1]], bijection[pair[0]]
        output.append(bijection)

    return output

# %% Create the constraints 
def genConstraint(bijection, element, result):
    #               name of bijection       element                   resulting action 
    output = "(" + str(bijection) + ", " + str(element) + ") --> " + str(result) + ", \n"
    return output

def make(bijections, n):
    constraints = []
    for bij in bijections:
        for element in bij:
            constraint = genConstraint(bijections.index(bij), bij.index(element), element)
            constraints.append(constraint)
            constraint = ""
    constraints = "".join(constraints)
    constraints = "letting n be " + str(n) + " \n" + "letting SGS be function (" + constraints + ")\n"+ "letting sizeS be " + str(len(bijections) - 1)
    return(constraints)

# %% Main
result = getContent()
# print(result)
n = getn()
# print(n)
bijections = genBijections(result,n)
# print (bijections)
constraints = make(bijections, n)
# print(constraints)

with open ('n.param', 'w') as f:
    f.write(constraints)
    f.close()