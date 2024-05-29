#!/usr/bin/bash

#module load openbabel/2.4.1
# conda activate extras

for i in *pdb
do
echo $i
babel $i -omol2 ${i%.pdb}.mol2 &>> output_mol2.log
done


