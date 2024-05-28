#! /bin/bash

#SBATCH --nodes=1
#SBATCH --job-name=BPREX
#SBATCH --partition=gpu2080
#SBATCH --gres=gpu:1 
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=4
##SBATCH --mem-per-cpu=2G 
#SBATCH --time=100:00:00
##SBATCH --output=slurm.out

#===============================================

export nnodes=`cat nnodes`
export nreps=`cat nreps`

export i=51
export eqS=1  # equilibration time (in ns)
export S=5  # total time in ns for each replicate 
export N=5  # total number of replicates

./postprocess.sh

