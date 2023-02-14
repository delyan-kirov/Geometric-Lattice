# %%
from array import *
from pathlib import Path
import random
# %%
def get_n():
    with open ("n.param", 'r') as f:
         data = f.read()
         n = data.split("letting n be ",1)[1]
         f.close()
    return int(n)

#%%
def rand_perm(n):
    perm = []
    while 0<1:
        number = random.randint(0,n-1)
        if number not in perm:
            perm.append(number)
        if len(perm) == n:
            break
    print(perm)
    return perm

#%%
def make_gap_file(path,n):
    data = "PrintTo(\"new.g\",StrongGeneratorsStabChain(StabChain(SymmetricGroup("
    base = str(rand_perm(n))
    # PrintTo("new.g",StrongGeneratorsStabChain(StabChain(SymmetricGroup(12),[0,1,2,3,4])));
    data = data + str(n) + ")," + base + ")));"
    with open("stabchain.gap", 'w') as file:
      file.write(data)


# %%
#Main
path = Path(".")
n = get_n()
make_gap_file(path, n)
