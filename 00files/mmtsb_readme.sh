#!/bin/bash

#rm *.psf *.crd *.pdb *.out

## charge on STARD11 = -3

## Ryan Hayes ==> maintain charge rather than counterbalance it.
## ARG-> ASN  ==> I will add an extra POT ion and couple it with ASN

#convpdb.pl -solvate -cutoff 10 -cubic -ions POT:4 -out charmm22 ../fromMahmoud/f_1600_arg478_popc155_hbonds_prepared_nopc.pdb > neutr-solv.pdb

#read 648 atoms, 216 residues from /Home/ii/parveeng/Softwares/toolset/data/water.pdb
#read 10887 atoms, 1570 residues from -
#box size: 96.631133 x 96.631133 x 96.631133

#convpdb.pl -segnames -nsel TIP3 -renumber 1 neutr-solv.pdb > solvent.pdb
#convpdb.pl -segnames -nsel CLA neutr-solv.pdb > ions.pdb
#convpdb.pl -segnames -nsel POT neutr-solv.pdb > ions.pdb

#sed -i "s/HETATM/ATOM  /g" ions.pdb

grep 'W00T' solvent.pdb > solvent00.pdb # apend END in last line
grep 'WT00' solvent.pdb > solvent01.pdb
grep 'WT01' solvent.pdb > solvent02.pdb # apend END in last line
grep 'WT02' solvent.pdb > solvent03.pdb
grep 'WT03' solvent.pdb > solvent04.pdb

#---------------------------------------------------------------------
## TEST

# HSD41 : ND1 = coordintes from complex.pdb and neutr-solvated.pdb
# HSD41: ND1 = complex coordinates - neutr-solvated coorintes
# convpdb.pl -translate 16.938 -27.032 0.406 neutr-solv.pdb > test1.pdb

#Calculate the RMSD difference without alignment between PROT from complex.pdb and test1.pdb

# It turn out that MMTSB only does translation when solvating the system.

