import ast

#%%
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
def clean_gap_data(gap_data):
    gap_data = gap_data.replace(" (), ", "").replace("\n", "")
    gap_data = ast.literal_eval(gap_data)
    return [(x-1,y-1) for x,y in gap_data]

#%%
def make_cons(gap_data, n):
    constraints = []
    for (a, b) in gap_data:
        result_string = f"({a}, {b}) --> {b},\n"
        constraints.append(result_string)
    constraints = "letting n be " + str(n) + "\n" + \
    "letting SGS be function(" + "".join(constraints[:-2]) + ")" + \
        "\nletting sizeS be " + str(len(constraints) - 3)
    return constraints

#%%
def add_cons_to_file(constraints):
    with open ("n.param", 'w') as file:
        file.write(constraints)
        file.close
    print("Done creating constraints.")
        

#%% Main
n = get_n()
gap_data = clean_gap_data(get_gap_file())
constraints = make_cons(gap_data, n)
add_cons_to_file(constraints)