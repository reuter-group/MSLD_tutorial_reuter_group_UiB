#!/bin/bash

while read mol sub1 sub2
do

while read p
do

export j=`awk -v a=$p '$2==a' "$mol"_s1s"$sub1"s2s"$sub2".dat | awk '{print $2}'`

#echo $p $j

if [ "$j" = "$p" ]; then
    echo "correct atoms founds corresponding to original mol2. " "$p" "$j" 
else
    echo "atom not found from rmsd calculation." "$p" ":from mol2 file" >> for_"$mol"_s1s"$sub1"s2s"$sub2".dat
fi


done < <(grep 'non1\|UNL\|LIG\|LIG1' tmp/"$mol".mol2 | sed '$ d' | awk '{print $2}') 

done < <(cat mol_list.txt)
