#!/bin/bash

# Sample shell script for running test cases that includes
# color coding some output.  Code modeled after code
# from Martin Nester

RED="\033[0;31m"
GREEN="\033[0;32m"
BOLD="\033[1m"
NC="\033[0m" # No Color
BLUE="\033[0;34m"
UL="\e[430m"

echo -e "${BOLD}Test cases:"
echo -e "\t${BOLD}test\tresult\truntime${NC}"

## 

PROG_TO_TEST=cs412_mingraphcolor_exact.py

cd test_cases

for test in test*
do
    cd $test 

    start=`python3 -c 'import time; print(time.time())'`
    python3 ../../${PROG_TO_TEST} < testInput.txt > testOutput.txt
    end=`python3 -c 'import time; print(time.time())'`
    runtime=$( echo "$end - $start" | bc -l )

    echo -e "\t${test}\t${GREEN}passed\t${BLUE}${runtime}s${NC}"


    cd ../
done

exit 0 
