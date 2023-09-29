#!/usr/bin/bash

echo Removing cached files
rm -r Output
mkdir Output
# Python environment
source ../pythonEnv/bin/activate
for n in {2..40}; do
    rm -r conjure-output
    echo
    echo "Setting n to $n"
    echo letting n be $n > n.param
    echo "Adding parameter $n"

    # Generate GAP constraints.
    python3 genStabChain.py

    gap -b -q << EOI
    Read("stabchain.gap");
    quit;
EOI
    python3 addGapConstraints.py
    # solving model
    conjure solve -ac --number-of-solutions=all --solver=nbc_minisat_all geo.essence n.param
    #Gather the data
    mkdir Result$n
    for file in *.solution
    do
      mv "$file" "Result$n"
    done 
    cp -r ./conjure-output ./Result$n
    mv ./Result$n ./Output
    ./countSyms.sh $n
    rm new.g 
    rm n.param 
    rm stabchain.gap
done
