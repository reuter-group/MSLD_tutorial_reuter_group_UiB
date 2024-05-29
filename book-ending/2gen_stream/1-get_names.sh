#!/bin/bash

while read mol sub1 sub2
do
cp $source/"$mol".mol2 .
cp $comboligs/s1s"$sub1".s2s"$sub2".pdb .

grep 'non1\|UNL\|LIG\|LIG1' "$mol".mol2 | sed '$ d' | awk '{print $2, $3, $4, $5}' > "$mol".xyz
grep 'ATOM' s1s"$sub1".s2s"$sub2".pdb  | awk '{print $3, $6, $7, $8}' > s1s"$sub1"s2s"$sub2".xyz

python get_rmsd.py s1s"$sub1"s2s"$sub2".xyz "$mol".xyz | awk '{print $8, $16}' |  sed 's/,/ /g' > "$mol"_s1s"$sub1"s2s"$sub2".dat

done < <(awk '{print $1, $2, $3}' mol_list.txt)

## check if all the atoms from original mol2 files have been read or not

mkdir -p tmp
mv *.pdb tmp/
mv *.mol2 tmp/
mv *.xyz tmp/
