#!/usr/bin/env bash

echo "adding parameter n" 

read -p 'Number of points (2 to 12 recommended)' param
echo
echo The parameter of choice was set to $param
if test $param -gt 100 
then
        echo "Too big, exit script!"
        exit 0
fi
if [[ $((param)) != $param ]]; then
    echo "Incorrect input, exit script!"
    exit 0
fi

echo "letting n be $param" > n_test.txt
mv -v "n_test.txt" "n_test".param

python3 add_sym_constraints.py

echo "solving lattice"

conjure solve -ac --number-of-solutions=all geo_sym.essence n_test.param

echo "running nauty"
python3 nauty.py

echo "running python"
python3 graph.py

echo "deleting solutions"
find -iname '*.solution' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.param' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.txt' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.cover' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
