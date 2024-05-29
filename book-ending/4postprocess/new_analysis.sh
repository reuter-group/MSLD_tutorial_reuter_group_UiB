#!/bin/bash

CHARMMEXEC=/net/orinoco/pga043/CHARMM_47a2/charmm_47a2/build_opls/charmm

#================= Analysis ==================================
# Get ith combination from combinations.txt
END=`wc -l ../combinations.txt | awk '{print $1}'`
for((i=1;i<=END;i++))
do
comb=`sed "${i}q;d" ../combinations.txt`
comb=($comb)

# Define substituents for each site
sub1=${comb[0]}
sub2=${comb[1]}

echo $sub1-$sub2

#change "dtype" for different systems.
#Also, modify the stream file in cg2og_energies.inp according to the system chosen
#for, dtype = water and prot, stream file = *crn2ff_qpert.str
#for, dtype = cg2ogwater & cg2ogprot, stream file = *ff2crn_qpert.str

# post-processing trajectory containing original force field-charges

$CHARMMEXEC build=prot_prep dtype=crn2ffprot sys=prot box=74.029177 nbond=prot sub1=$sub1 sub2=$sub2 -i postprocess_ff.inp #> junk_crn2ffprot_s1s"$sub1".log  

#$CHARMMEXEC build=water_prep dtype=crn2ffwater sys=water box=34.633512 nbond=water sub1=$sub1 sub2=$sub2 -i postprocess_ff.inp

#grep 'GPU error' junk*.log

## **************************************************
## post-processing trajectory containing renormalized charges

$CHARMMEXEC build=prot_prep dtype=prot box=74.029177 nbond=prot sub1=$sub1 sub2=$sub2 -i postprocess_renormal.inp #> junk_prot_s1s"$sub1".log  

#$CHARMMEXEC build=water_prep dtype=water sys=water box=34.633512 nbond=water sub1=$sub1 sub2=$sub2 -i  postprocess_renormal.inp

#----------------------------------------------------------
#=========================================================

#for j in crn2ffprot prot
#do

#$CHARMMEXEC build=prot_prep dtype="$j" sub1=$sub1 -i rmsf_ligand.inp

#done
done

#===============================================


