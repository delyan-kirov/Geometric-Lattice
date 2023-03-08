#!/usr/bin/env bash
start_time=$(date +%s.%3N)

python3 lattice.py

echo "solving lattice"

conjure solve -ac --number-of-solutions=all boolean.essence n.param

end_time=$(date +%s.%3N)
elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo "It took " $elapsed "to solve the model" 

restart_time=$(date +%s.%3N)

echo "running nauty"
#python3 nauty.py

new_time=$(date +%s.%3N)
reelapsed=$(echo "scale=3; $new_time - $restart_time" | bc)
echo "It took "$reelapsed "to remove isomorphic images."

echo "running python"
python3 graph.py

echo "deleting solutions"
find -iname '*.solution' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.param' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.txt' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.cover' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
#rm geo_sym.essence
