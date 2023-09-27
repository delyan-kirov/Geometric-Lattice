#!/usr/bin/env bash

file=./Output/"Result$1"
echo Coppy solutions to file: "$file"
cp -r nauty/* $file
cd $file
./findIsoClasses.sh
echo done 
