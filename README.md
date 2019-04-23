# Supermarket-Optimization

This program lists the groups of item numbers (group size 3) that appear together at least a certain number of times in the .dat file. The number of times is determined by the input of sigma.

In order to run this program, do the following:
  - Clone or download the repository
  - The globality_supermarket.py file is the file you want to execute from terminal
  - Go to terminal, and run "python globality_supermarket.py -f <dat file path> <sigma> "
        - For example, "python globality_supermarket.py -f /Users/bob/Downloads/retail_25k.dat 4"
        - The sigma value is 4 and the file path is /Users/bob/Downloads/retail_25k.dat
  - After executing, a textfile called "supermarket_optimization.txt" will appear in the same directory you executed the script in.
  - The textfile will have a header and below it will be all of the desired data. 
