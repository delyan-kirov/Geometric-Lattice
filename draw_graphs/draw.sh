#!/usr/bin/env bash

echo "adding parameter n" 

echo "letting n be 6" > n_test.txt
mv -v "n_test.txt" "n_test".param

echo "solving lattice"

conjure solve -ac --number-of-solutions=all geo_sym_test.essence n_test.param

find -iname '*.param' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l

for file in *.solution; do
   echo "letting n be 6" >> $file
done

echo "changing file type"

for file in *.solution; do 
    mv -- "$file" "${file%.solution}.param"
done

python3 rename_files.py

echo "finding cover"

for file in *.param; do
    conjure solve -ac cover.essence $file
done

echo "running python"

python3 graph.py

echo "deleting solutions"
find -iname '*.solution' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.param' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
