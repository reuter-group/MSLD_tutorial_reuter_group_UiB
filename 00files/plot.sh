#!/bin/bash

END=30
for((i=26;i<=END;i++))
do
cd analysis"$i"
python ../multisite_matlab.py
cd ../
done
