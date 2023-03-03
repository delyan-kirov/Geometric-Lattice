# %%
import os

# %%
path = "." #current directory
count = 0

# %%
#main
def sol_count(count, path):
  for root, dirs, files in os.walk(path):
    for file in files:    
      if file.endswith('.solution'):
        count = count + 1
  print("number of conjure solutions is " + str(int(count/2)))
  return count

sol_count(count, path)


