#!/usr/bin/env bash
start_time=$(date +%s.%3N)
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

echo "letting n be $param" > n.txt
mv -v "n.txt" "n".param

python3 gap_constraints.py
gap stabchain.gap
pkill gap
python3 gap.py

echo "solving lattice"

conjure solve -ac --number-of-solutions=all geo.essence n.param

end_time=$(date +%s.%3N)
elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo "It took " $elapsed " to solve the model" 

restart_time=$(date +%s.%3N)

echo "running nauty"
python3 nauty.py

new_time=$(date +%s.%3N)
reelapsed=$(echo "scale=3; $new_time - $restart_time" | bc)
echo "It took "$reelapsed " remove isomorphic images."

echo "running python"
python3 graph.py

echo "deleting solutions"
find -iname '*.solution' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.param' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.txt' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.cover' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
