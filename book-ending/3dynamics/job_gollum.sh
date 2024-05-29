#!/bin/bash
#SBATCH --nodes=1
#SBATCH --job-name=prot
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
##SBATCH --mem-per-cpu=2G 
#SBATCH --time=100:00:00
##SBATCH --output=slurm.out
#SBATCH --array=1-10
#SBATCH --export=ALL

#===============================================
ml charmm/c49a1_anaconda/c49a1
export charmm=/export/apps/CentOS7/charmm/c49a1/bin/charmm

export i=$SLURM_ARRAY_TASK_ID

while read p q
do

export dtype="$p"
export nbond="$q"

comb=`sed "${i}q;d" ../combinations.txt`
comb=($comb)

# Define substituents for each site
sub1=${comb[0]}
sub2=${comb[1]}

echo site1sub"$sub1"-site2sub"$sub2"

echo "CHARMM executable is ${CHARMMEXEC}"
echo "ligand combination is ${comb}"
echo "dtype is ${dtype}"

if [ ! -d "dynamics-s1s${sub1}.s2s${sub2}" ]
then
    mkdir dynamics-s1s${sub1}.s2s${sub2}
fi

if [ ! -d "dynamics-s1s${sub1}.s2s${sub2}/${dtype}" ]
then
    mkdir dynamics-s1s${sub1}.s2s${sub2}/${dtype}
fi

# Run dynamics
mpirun -np 1 -x OMP_NUM_THREADS=8 --bind-to none --map-by node $CHARMMEXEC sub1=$sub1 sub2=$sub2 dtype=${dtype} nbond=${nbond} seed=$RANDOM -i domdec_${dtype}.inp #-o ${dtype}_dyn-s1s${sub1}.out


#------- finished ------------------

done < <(awk '{print $1, $2}' tmp.dat  | sed -n '4p')

