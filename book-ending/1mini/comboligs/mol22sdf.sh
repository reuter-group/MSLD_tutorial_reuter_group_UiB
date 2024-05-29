#!/usr/bin/bash

#module load openbabel/2.4.1
# conda activate extras

for i in *mol2
do
echo $i
babel $i -osdf ${i%.mol2}.sdf &>> output_sdf.log
done


