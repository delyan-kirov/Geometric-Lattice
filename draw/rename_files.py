# %%
import re
import networkx as nx
import math
from pathlib import Path
import matplotlib.pyplot as plt
import os

# %%
path = Path(".")  # current directory
extension = ".param"
count = 0
for files in os.listdir(path):
    count = count + 1
    if files.endswith(extension):
        name = str(count) + '.param'
        os.rename(files, name)


