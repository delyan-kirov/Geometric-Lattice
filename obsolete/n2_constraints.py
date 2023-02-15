# %%
import os
import re
from pathlib import Path

# %%
def make_content (n):
    content = '\n'
    for i in range(1,n-2):
        for j in range(1,n-1):
            if (j > i):
                content = content + "[M((i," + str(i) + ")) | i:N] " + ">=lex" + " [M((i," + str(j) + ")) | i:N] \/ " + \
                             "(R(" + str(i) + ") !=" + "R(" + str(j) + "))," + "\n"
    print("adding symmetry constraints")
    return content

# %%
def get_n():
    with open ("n.param", 'r') as f:
         data = f.read()
         n = data.split("letting n be ",1)[1]
    return int(n)

# %%
path = Path(".")
n = get_n()
content = make_content(n)
with open("geo.essence", 'r') as f:
    with open("geo_sym.essence", 'w') as g:
        g.write(f.read())
        g.close
    with open("geo_sym.essence", 'a') as g:
        g.write(content)
    f.close()


