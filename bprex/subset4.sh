#!/bin/bash

#SBATCH --nodes=1
#SBATCH --job-name=bprex
#SBATCH --partition=gpu2080
#SBATCH --gres=gpu:3
#SBATCH --tasks-per-node=3
#SBATCH --cpus-per-task=8

##SBATCH --mem-per-cpu=2G 
#SBATCH --time=100:00:00
##SBATCH --output=slurm.out
#DEPEND="--dependency=afterok:789701"
###EXCLUDE="--exclude=gollum000"
# NICE="--nice=500"
##RE_Q="--no-requeue"
## array => 1-10: 5 ns for each replicate, 1-25: 25 ns for each replicate
#SBATCH --array=1-5%1
#SBATCH --export=ALL

#===============================================
ml load openmm/7.6.0 #gcc/10.2.0 fftw/3.3.8 cuda/11.2
ml load openmpi/3.1.2-gcc-10.2.0

#export nnodes=`cat nnodes`
#export nreps=`cat nreps`
#export nitt=1

#for p in a b c d e
#do

#export ini=71
#export i=$ini$p

./runset4_rx.sh

#done
