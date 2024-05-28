#!/bin/bash
#Analysis part requires python2 so execute conda activate py2

#CHARMMEXEC=/net/orinoco/pga043/CHARMM_47a2/charmm_47a2/build_blade_repdstr/charmm
CHARMMEXEC=/net/orinoco/pga043/CHARMM_47a2/charmm_47a2/build_domdec_repdstr/charmm

DIR=`pwd`

name=`cat name`
nnodes=`cat nnodes`
nreps=`cat nreps`

ini=13  # phase 2 starts with this #
iri=1
ifi=40 # phase 2 ends with this #

for i in `seq $ini $ifi`
do

im1=$(( $i - 1 ))
ip1=$(( $i + 1 ))
im5=`awk 'BEGIN {if (('$i'-4)<'$iri') {print '$iri'} else {print '$i'-4}}'`
N=$(( $i - $im5 + 1 ))
ir=$(( $RANDOM % ( $ip1 - $iri ) + $iri ))

RUNDIR=$DIR/run$i
PANADIR=$DIR/analysis$im1
ANADIR=$DIR/analysis$i

while [ ! -f $ANADIR/b_sum.dat ]
do

if [ -d ${RUNDIR}_failed ]; then
  rm -r ${RUNDIR}_failed
fi
if [ -d $RUNDIR ]; then
  cp -r $RUNDIR ${RUNDIR}_failed
  rm -r $RUNDIR
  echo "run$i failed"
  sleep 30
fi

### Run the simulation
mkdir $RUNDIR
mkdir $RUNDIR/res $RUNDIR/dcd
cp -r variables$i.inp prep $RUNDIR/
cd $RUNDIR

### timeout -s SIGINT 8h
echo "run$i started"
mpirun -np 3 -x OMP_NUM_THREADS=8 --bind-to none --map-by node $CHARMMEXEC iflat=$i esteps=15000 nsteps=50000 seed=$RANDOM -i ../msld_flat.inp > output 2> error

#mpirun -n 3 $CHARMMEXEC iflat=$i esteps=15000 nsteps=50000 seed=$RANDOM -i ../msld_flat.inp > output 2> error

pid1=$!
wait $pid1

#sed -i '/run setvariable domdecheuristic off/,$d' output

#===================================================
mv res/lmnmt_flat.lmd_0_0 res/lmnmt_flat.lmd_0
mv res/lmnmt_flat.lmd_1_1 res/lmnmt_flat.lmd_1
mv res/lmnmt_flat.lmd_2_2 res/lmnmt_flat.lmd_2

mv lmnmt_heat.rex_0_0 lmnmt_heat.rex_0
mv lmnmt_heat.rex_1_1 lmnmt_heat.rex_1
mv lmnmt_heat.rex_2_2 lmnmt_heat.rex_2


mv lmnmt_flat.rex_0_0 lmnmt_flat.rex_0
mv lmnmt_flat.rex_1_1 lmnmt_flat.rex_1
mv lmnmt_flat.rex_2_2 lmnmt_flat.rex_2
#===================================================


rm -rf prep
cd $DIR


# Run the analysis
echo "analysis$i started"
if [ ! -d $ANADIR ]; then
  mkdir $ANADIR
fi
mkdir $ANADIR/
cp $PANADIR/b_sum.dat $ANADIR/b_prev.dat
cp $PANADIR/c_sum.dat $ANADIR/c_prev.dat
cp $PANADIR/x_sum.dat $ANADIR/x_prev.dat
cp $PANADIR/s_sum.dat $ANADIR/s_prev.dat
cd $ANADIR


../ALF/GetLambdas.py $i
../ALF/GetEnergy.py $im5 $i
../ALF/RunWham.sh $(( $N * $nreps )) `cat ../ntersiteflat`
../ALF/GetFreeEnergy5.py 0 1 `cat ../ntersiteflat`
../ALF/SetVars.py $ip1
echo "set restartfile = \"run$ir/res/${name}_flat.res" >> $DIR/variables$ip1.inp
#echo "trim restartfile from 2" >> $DIR/variables$ip1.inp


cd $DIR

done

done
