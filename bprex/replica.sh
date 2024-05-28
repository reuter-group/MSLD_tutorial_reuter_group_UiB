#!/bin/bash

export nnodes=`cat nnodes`
export nreps=`cat nreps`
export nitt=1

for p in a b c d e
do

export ini=51
export i=$ini$p

#./runset4.sh
sbatch subset4.sh

done

