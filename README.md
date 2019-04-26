# Supermarket-Optimization

This program helps determine which sets of three items in a supermarket should be grouped together to maximize sales. It takes in a ".dat" transaction log file and outputs the desired results depending on the sigma value that you set. The sigma value determines the minimum frequency that a set of three items must show up together in order to be written out to the output file. 

You will notice in the source code that there are a couple optimizations done to shave off some fractions of seconds.

In order to run this program, do the following:
  - Clone or download the repository
  - The globality_supermarket.py file is the file you want to execute from terminal
  - Go to terminal, and run "python globality_supermarket.py -f <dat file path> <sigma> "
        - For example, "python globality_supermarket.py -f /Users/bob/Downloads/retail_25k.dat 4"
        - The sigma value is 4 and the file path is /Users/bob/Downloads/retail_25k.dat
  - After executing, a textfile called "supermarket_optimization.txt" will appear in the same directory you executed the script in.
  - The textfile will have a header and below it will be all of the desired data. 
