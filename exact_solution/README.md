## Running test cases

To run the test cases you should be in an environment that allows you to execute bash files. For me I used WSL, but any linux based system should suffice.\
Once you are in the proper environment you can run the script by typing ./run_test_cases.sh in the exact_solution folder and pressing enter.

## 20 minute test case

The testInput.txt file in the directory test_cases/test20min holds the input that causes the program to run for longer than 20 minutes.\
This happens because the input is a large complete graph, this kind of graph gives my program an exceptionally hard time because it\
must try every combination of colors from 2 up to _n_ verticies!

## Small test cases

The smaller test cases (every test in test_cases other than test20min) all include example inputs with far fewer verticies and non complete graphs.