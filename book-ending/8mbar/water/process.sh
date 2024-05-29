#!/bin/bash

while read p q
do

export dir=/net/orinoco/pga043/MSLD/bergen-4/2/hne/book-ending/3dynamics/dynamics-s1s"$p".s2s"$q"/
echo '**************************'
echo "$dir"
echo '=========================='

python convergence.py "$dir" "$p" "$q"

#python plot.py "$dir" "$p" "$q"

done < <(cat ../../combinations.txt)


