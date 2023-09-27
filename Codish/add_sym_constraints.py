# %%
import os
import re
from pathlib import Path

# %%
def make_content (n):
    content = '\n'
    for i in range(1, n-2):
        #[M((i,1)) | i:N] >=lex [M((i,2)) | i:N],
         content = content + "[M((i," + str(i) + ")) | i:N] " + ">=lex" + " [M((i," + str(i+1) + ")) | i:N] \/ " + \
                             "(R(" + str(i) + ") !=" + "R(" + str(i+1) + "))," + "\n"
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


