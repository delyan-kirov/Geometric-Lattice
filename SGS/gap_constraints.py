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
    data = "moregens := function(G, list) \n local gens, i, Gs, orb, o; gens := []; for i in [1..Length(list)] do Gs := Stabilizer(G, list{[1..i-1]}, OnTuples); orb := Orbit(Gs, list[i]); for o in orb do AddSet(gens, RepresentativeAction(Gs, list[i], o)); od; od; return gens; end; " + "\n"
    base = "[1.." + str(n) + "]"
    #moregens(SymmetricGroup(8), [1..8]);
    # PrintTo("new.g",StrongGeneratorsStabChain(StabChain(SymmetricGroup(12),[0,1,2,3,4])));
    func = "PrintTo(\"new.g\",moregens(SymmetricGroup(" + str(n) + ")," + base + "));"
    data = data + func
    with open("stabchain.gap", 'w') as file:
      file.write(data)


# %%
#Main
path = Path(".")
n = get_n()
make_gap_file(path, n)
