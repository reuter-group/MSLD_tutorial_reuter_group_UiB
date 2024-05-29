#!/usr/bin/bash

# File changed to run on RTX3080/Macbook ##

# Figure out number of combinations/minimizations
nsubs=(`cat nsubs`)
nligs=1
for i in ${nsubs[@]}; do let nligs=($nligs * $i)


### --error=mini_%A_%a.err --output=mini_%A_%a.out --time=01:00:00 --partition=brooks --ntasks=1 --array=1-${nligs}%15
./combo_mini.batch #> mini.out 2> mini.err

done

