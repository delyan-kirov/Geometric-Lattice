#!/usr/bin/env bash

for param in {1..12}
do
  echo "letting n be $param" > n.txt
  mv -v "n.txt" "n".param
  bash draw.sh
  echo -e
done
