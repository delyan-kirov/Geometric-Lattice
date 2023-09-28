#!/usr/bin/env bash
start_time=$(date +%s.%3N)

echo "adding parameter n" 
cat n.param >> output
python3 codish.py
python3 gap_constraints.py >> output

gap -b -q << EOI
Read("stabchain.gap");
quit;
EOI
python3 gap.py >> output

echo "solving lattice"

conjure solve -ac --number-of-solutions=all geo_sym.essence n.param

python3 solution_count.py >> output

end_time=$(date +%s.%3N)
elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo "It took " $elapsed " to solve the model"  >> output

restart_time=$(date +%s.%3N)

echo "running nauty"
python3 nauty.py >> output

new_time=$(date +%s.%3N)
reelapsed=$(echo "scale=3; $new_time - $restart_time" | bc)
echo "It took "$reelapsed " to remove isomorphic images." >> output

echo "running python"
python3 graph.py >> output

echo "deleting cached files"
find -iname '*.solution' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.param' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l
find -iname '*.txt' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l

echo -e >> output
find -iname '*.cover' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l

bash delete.sh
