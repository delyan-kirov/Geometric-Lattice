#!/usr/bin/env bash

echo "deleting images"
find -iname '*.png' -type f -print0  | xargs --null -n 100 rm -vrf | wc -l