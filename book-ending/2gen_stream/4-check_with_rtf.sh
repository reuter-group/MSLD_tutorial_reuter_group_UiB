#!/bin/bash

while read mol sub1 sub2
do

echo site1sub"$sub"site2sub"$sub2"

while read charge name
do

export compare=`grep -i atom $rtfs/"$mol".rtf |  awk -v a="$charge" '$4==a' | awk '{print $2, $3, $4}'`

echo charge=$charge new_name=$name OPLS=$compare

done < <(grep 'scalar' s1s"$sub1".s2s"$sub2"_crn2ff_qpert.str  | awk '{print $4, $9}')

echo '*=================================*'
echo '*=================================*'

done < <(awk '{print $1, $2, $3}' mol_list.txt) 
