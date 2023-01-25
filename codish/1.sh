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
