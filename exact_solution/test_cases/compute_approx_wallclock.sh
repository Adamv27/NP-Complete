#!/bin/bash

DIR="./timing"

for input in "$DIR"/*
do
    input_size=$(head -n 1 "$input")
    run_time=$(/usr/bin/time -f "%e" python3 ./cs412_mingraphcolor_exact.py < "$input" 2>&1 > /dev/null)
    
    echo "N: $input_size time: $run_time" 
done
