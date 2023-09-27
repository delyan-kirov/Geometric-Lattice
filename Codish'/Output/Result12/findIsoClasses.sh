#!/usr/bin/bash

rm -f data.g 

for file in *.solution; do 
  python3 genGapData.py "$file" 
done

# Append graps to Graph array inside data.g 
awk '{ arr[NR] = $1 }
     END {
         printf("Lattices := [")
         for (i = 1; i < NR; i++) {
             printf("%s, ", arr[i])
         }
         if (NR > 0) {
             printf("%s", arr[NR])
         }
         printf("];\n")
     }' data.g >> data.g
# Append functions to data.g
echo 'LoadPackage("yags");' >> data.g
cat function.g >> data.g

gap -b -q << EOI
LoadPackage("yags");
Read("data.g");
quit;
EOI
echo -e
echo -n "number of solutions is: "; cat result.g | tr -d '\n'; echo

#cat result.g
