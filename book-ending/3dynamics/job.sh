#!/bin/bash

END=2 #`wc -l tmp.dat | awk '{print $1}'`
for((i=1;i<=END;i++))
do

junk=`sed "${i}q;d" tmp.dat`
junk=($junk)

# Define substituents for each site
export dtype=${junk[0]}
export nbond=${junk[1]}

echo $dtype $nbond

bash dynamics.batch #>> "$dtype".out 2>> "$dtype".err

done

#-------------------

#while read p q 
#do
#export dtype=$p
#export nbond=$q

#echo $p $q

#bash dynamics.batch >> "$dtype".out 2>> "$dtype".err

#done < <(cat tmp.dat)

