#!/bin/bash

while read mol sub1 sub2
do
echo '* Change atom charges to original ff charges for ligand s1s'"$sub1".s2s"$sub2" > s1s"$sub1".s2s"$sub2"_crn2ff_qpert.str
echo '*' >> s1s"$sub1".s2s"$sub2"_crn2ff_qpert.str
echo >> s1s"$sub1".s2s"$sub2"_crn2ff_qpert.str

#--------------------------------------------
while read pdb mol2 
do

export ff_charge=`grep -i atom $rtfs/"$mol".rtf |  awk -v a="$mol2" '$2==a' | awk '{print $4}'`

#echo $pdb "$ff_charge"

echo scalar charge set "$ff_charge" sele atom LIG 1 "$pdb" end >> s1s"$sub1".s2s"$sub2"_crn2ff_qpert.str

done < <(awk '{print $1, $2}'  "$mol"_s1s"$sub1"s2s"$sub2".dat)
#----------------------------------------

echo >> s1s"$sub1".s2s"$sub2"_crn2ff_qpert.str
echo RETURN >> s1s"$sub1".s2s"$sub2"_crn2ff_qpert.str


done < <(awk '{print $1, $2, $3}' mol_list.txt)
