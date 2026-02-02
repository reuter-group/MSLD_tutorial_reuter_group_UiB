#!/bin/bash

export cgenff=/net/orinoco/apps/silcsbio.2024.1/cgenff/cgenff

while read p
do

$cgenff -v "$p".mol2 > "$p".str

sed -n -e '/Toppar/,/END/ p' "$p".str > "$p".rtf
sed -n -e '/flex/,/RETURN/ p' "$p".str > "$p".prm   

done < <(cat mol_list.txt)
