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

def make_gap_file(path,n):
    data = "PrintTo(\"new.g\",StrongGeneratorsStabChain(StabChain(SymmetricGroup("
    base = str(list(range(1, n+1)))
    # PrintTo("new.g",StrongGeneratorsStabChain(StabChain(SymmetricGroup(12),[0,1,2,3,4])));
    data = data + str(n) + ")," + base + ")));"
    with open("stabchain.gap", 'w') as file:
      file.write(data)


# %%
#Main
path = Path(".")
n = get_n()
make_gap_file(path, n)
