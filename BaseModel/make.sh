#!/usr/bin/env bash

source ../pythonEnv/bin/activate
mkdir Output

for n in {2..40}
do
  rm -r conjure-output 
  echo "letting n be "$n > n.param
  cat n.param
  python3 add_sym_constraints.py
  conjure solve -ac --number-of-solutions=all --solver=nbc_minisat_all geo.essence n.param
  mkdir Result$n
  for file in *.solution
  do
    mv "$file" "Result$n"
  done 
  cp -r ./conjure-output ./Result$n
  mv ./Result$n ./Output
  ./countSyms.sh $n
done

