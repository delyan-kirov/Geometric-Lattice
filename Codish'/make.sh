#!/usr/bin/env bash

mkdir Output

for n in {2..6}
do
  echo "letting n be "$n > n.param
  conjure solve -ac --number-of-solutions=all --solver=nbc_minisat_all geo.essence n.param
  mkdir Result$n
  for file in *.solution
  do
    mv "$file" "Result$n"
  done 
  cp -r ./conjure-output ./Result$n
  mv ./Result$n ./Output
done

