#!/usr/bin/env bash
rm output
for param in {18..22}
do
  echo "letting n be $param" > n.txt
  mv -v "n.txt" "n".param
  bash draw.sh
  echo -e
done
