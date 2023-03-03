#!/usr/bin/env bash
rm output
for param in {8..18}
do
  echo "letting n be $param" > n.txt
  mv -v "n.txt" "n".param
  bash draw.sh
  echo -e
done
