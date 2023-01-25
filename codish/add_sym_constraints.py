# %%
import os
import re
from pathlib import Path

# %%
def make_content (n):
    content = '\n'
    # (exists k: N. (forAll l: int(0..k-1). (M((l,i)) = M((l,j))) ) /\ (M((k,i)) > M((k,j))) ) \/ !(R(i) = R(i+1))
    for i in range(1, n-2):
         content = content + "( exists k: N. (forAll l: int(0..k-1). (M((l," + str(i) + ")" + \
         ")) = M((l," + str(i+1) + "))) /\ (M((k," + str(i) + ")) > M((k," + str(i+1) + "))) )" + \
         " \/ !(R(" + str(i) + ")" " = R(" + str(i+1) + "))," + '\n'
    print("adding symmetry constraints")
    return content

# %%
def get_n():
    with open ("n_test.param", 'r') as f:
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


